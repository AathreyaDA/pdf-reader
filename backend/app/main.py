from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="Knowledge Base AI",
    version="1.0.0",
    description="Chat with your documents."
)

app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "Knowledge Base AI backend is running!"
    }