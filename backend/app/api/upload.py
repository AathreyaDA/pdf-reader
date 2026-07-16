from fastapi import APIRouter, UploadFile, File

from app.services.pdf import save_pdf
from app.services.pdf import extract_text

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