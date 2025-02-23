from fastapi import FastAPI, Depends, HTTPException, Header
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY_CREDITS = {os.getenv("API_KEY"): 5}
print(API_KEY_CREDITS)
api_app = FastAPI()

def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key, or no credits")

    return x_api_key

@api_app.post("/generate")
def generate(prompt: str, x_api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[x_api_key] -= 1
    print("request received")
    llm = ChatGroq(api_key=os.getenv("API_KEY"))
    response = llm.invoke(prompt)
    return {"response": response.content}