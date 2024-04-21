# Fact-Extraction from Call-log

![image](https://github.com/krushikagujarati/Fact-Extraction-App/assets/48424819/21f778bc-59c9-4cda-95b5-d6b2c879bb35)

![image](https://github.com/krushikagujarati/Fact-Extraction-App/assets/48424819/b3c1819b-bd0d-4cae-a0e2-3e5d2fe37d52)

## Project Overview
This Call Log Analyzer App helps users to quickly extract important information from call logs using OpenAI's GPT-4 model. The application is built using FastAPI for the backend to manage data processing efficiently, and React for the frontend to provide a user-friendly interface.

## Technologies Used
1. Backend: FastAPI
2. Frontend: React
3. AI Model: OpenAI GPT-4

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

**Setting Up the Backend**

Navigate to the backend directory:
```
cd path_to_backend
```
**Install the required Python dependencies**
```
pip install fastapi uvicorn requests openai
```
**Start the backend server**
```
uvicorn main:app --reload
```
This will start the FastAPI server on http://localhost:8000.


**Setting Up the Frontend**

Navigate to the frontend directory:
```
cd path_to_frontend
```
**Install the required Node.js packages:**
```
npm install
```

**Start the frontend application:**
```
npm start
```

This will run the React app in the development mode and open http://localhost:3000 in your browser.

## Usage
Once both the frontend and backend are running:

Open your web browser to http://localhost:3000.
Enter your question, and the URLs of the call logs into the respective fields.
Submit the form and view the extracted facts displayed on the page.
