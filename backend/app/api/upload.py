from fastapi import APIRouter, UploadFile, File, Query

from app.services.pdf import save_pdf
from app.services.pdf import extract_text
from app.services.chunking import chunk_text
from app.services.embedding import save_embeddings

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
def upload_pdf(file: UploadFile = File(...)):
    path = save_pdf(file)

    return {
        "filename": path.name,
        "status": "uploaded"
    }


@router.post("/read")
def read_pdf(file: UploadFile = File(...)):
    text = extract_text(file)

    return {
        "text": text
    }


@router.post("/chunks")
def chunk_pdf(
    file: UploadFile = File(...),
    chunk_size: int = Query(
        default=1000,
        ge=100,
        le=5000,
        description="Maximum characters per chunk"
    )
):
    text = extract_text(file)
    
    chunks = chunk_text(text, chunk_size)

    return {
        "chunk_size" : chunk_size,
        "num_chunks" : len(chunks),
        "chunks" : chunks
    }


@router.post("/embed")
def embed_pdf(
    file: UploadFile = File(...),
    chunk_size: int = Query(default=1000, ge=100, le=5000)
):
    text = extract_text(file)

    chunks = chunk_text(text, chunk_size)

    embeddings = save_embeddings(chunks)

    return {
        "num_chunks": len(embeddings),
        "saved": True
    }