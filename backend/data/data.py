from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],  # Allows all origins from localhost:3000
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/call_log_gfsfdfd.txt")
async def get_call_log1():
    call_log_data = """
    1
    00:01:11,430 --> 00:01:40,520
    John: Hello, everybody. Let's start with the product design discussion. I think we should go with a modular design for our product. It will allow us to easily add or remove features as needed.

    2
    00:01:41,450 --> 00:01:49,190
    Sara: I agree with John. A modular design will provide us with the flexibility we need. Also, I suggest we use a responsive design to ensure our product works well on all devices. Finally, I think we should use websockets to improve latency and provide real-time updates.

    3
    00:01:49,340 --> 00:01:50,040
    Mike: Sounds good to me. I also propose we use a dark theme for the user interface. It's trendy and reduces eye strain for users. Let's hold off on the websockets for now since it's a little bit too much work.
    """
    return PlainTextResponse(content=call_log_data)

@app.get("/call_log_sdfqwer.txt")
async def get_call_log2():
    call_log_data = """
    1
    00:01:11,430 --> 00:01:40,520
    John: After giving it some more thought, I believe we should also consider a light theme option for the user interface. This will cater to users who prefer a brighter interface.

    2
    00:01:41,450 --> 00:01:49,190
    Sara: That's a great idea, John. A light theme will provide an alternative to users who find the dark theme too intense.

    3
    00:01:49,340 --> 00:01:50,040
    Mike: I'm on board with that.

    """
    return PlainTextResponse(content=call_log_data)

@app.get("/call_log_fdadweq.txt")
async def get_call_log3():
    call_log_data = """
    1
    00:01:11,430 --> 00:01:40,520
    John: I've been thinking about our decision on the responsive design. While it's important to ensure our product works well on all devices, I think we should focus on desktop first. Our primary users will be using our product on desktops.

    2
    00:01:41,450 --> 00:01:49,190
    Sara: I see your point, John. Focusing on desktop first will allow us to better cater to our primary users. I agree with this change.

    3
    00:01:49,340 --> 00:01:50,040
    Mike: I agree as well. I also think the idea of using a modular design doesn't make sense. Let's not make that decision yet.
    """
    return PlainTextResponse(content=call_log_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

