from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os, uvicorn

load_dotenv()

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")
memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory)

class Msg(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Msg):
    return {"reply": chain.predict(input=msg.message)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)