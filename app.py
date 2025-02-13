from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Message(BaseModel):
  user: str
  message: str

@app.post("/chat")
async def chat(message: Message):
  if message.message.lower() == "oi":
    return {
      "bot": f"Olá {message.user}, tudo bem?"
    }
  return {
    "bot": "Desculpe, só sei responder 'oi'"
  }

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)