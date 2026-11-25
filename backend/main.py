from fastapi import FastAPI

app = FastAPI(
    title="AI Community Assistant",
    description="Backend de AI Community Lab",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "project": "AI Community Assistant",
        "status": "online",
        "message": "Backend funcionando correctamente"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
