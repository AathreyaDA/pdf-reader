from fastapi import APIRouter, UploadFile, File

from app.services.pdf import save_pdf

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