from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/")
def chat_status():
    return {
        "status": "Chat endpoint works!"
    }