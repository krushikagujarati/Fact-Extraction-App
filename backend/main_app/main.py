from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import List, Optional
import requests
import openai
import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

url = 'https://api.openai.com/v1/chat/completions'

class SubmitQuestionDocs(BaseModel):
    question: str
    documents: List[str]

class GetQuestionAndFactsResponse(BaseModel):
    question: str
    facts: Optional[List[str]]
    status: str

database = {}

@app.post("/submit_question_and_documents")
async def submit_question_and_docs(data: SubmitQuestionDocs, background_tasks: BackgroundTasks):
    database['question'] = data.question
    database['facts'] = []
    database['status'] = 'processing'
    print("data=>",data)
    background_tasks.add_task(process_documents, data.question, data.documents)
    return {"message": "Processing started"}

async def process_documents(question: str, documents: List[str]):
    try:
        all_facts = []
        for url in documents:
            response = requests.get(url)
            if response.status_code == 200:
                extracted_facts = extract_facts(question, response.text)
                all_facts.extend(extracted_facts)
            else:
                raise HTTPException(status_code=404, detail=f"Document at {url} not found")
        
        database['facts'] = all_facts
        database['status'] = 'done'
    except Exception as e:
        print("err=>",e)
        database['status'] = 'error'
        database['error'] = str(e)

def extract_facts(question: str, text: str) -> List[str]:
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('API_key')}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": f"Question: {question}\nText: {text}\nExtract facts:"
        }
        ],
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }

    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Response from OpenAI:", response.json())
        print('\n')
        print(response.json()['choices'][0]['message']['content'])
        lines = response.json()['choices'][0]['message']['content'].split('\n')
        lines = [line.strip() for line in lines if line.strip()]
        return lines

@app.get("/get_question_and_facts")
def get_question_and_facts() -> GetQuestionAndFactsResponse:
    return GetQuestionAndFactsResponse(
        question=database.get('question', ''),
        facts=database.get('facts', []),
        status=database.get('status', 'error')
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
