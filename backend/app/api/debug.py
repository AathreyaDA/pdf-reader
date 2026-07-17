from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding import embed_text
from app.services.retrieval import cosine_similarity

router = APIRouter(
    prefix="/debug",
    tags=["Debug"]
)


class CompareRequest(BaseModel):
    text1: str
    text2: str


@router.post("/compare")
def compare(req: CompareRequest):

    embedding1 = embed_text(req.text1)
    embedding2 = embed_text(req.text2)

    similarity = cosine_similarity(
        embedding1,
        embedding2
    )

    return {
        "similarity": similarity,
        "embedding_dimensions": len(embedding1),
        "embedding1_preview": embedding1[:5],
        "embedding2_preview": embedding2[:5]
    }