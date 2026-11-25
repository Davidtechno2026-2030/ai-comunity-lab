from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(
    title="AI Community Assistant",
    description="Backend de AI Community Lab",
    version="0.4.0"
)

PROJECT_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = PROJECT_DIR / "index.html"


class ChatMessage(BaseModel):
    message: str


@app.get("/")
def home():
    return FileResponse(INDEX_FILE)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/chat")
def chat(data: ChatMessage):
    return {
        "response": f"Has escrito: {data.message}",
        "status": "success"
    }
