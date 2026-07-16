from pathlib import Path
import shutil

import pymupdf
from fastapi import HTTPException

UPLOAD_DIR = Path("uploads")


def save_pdf(file):
    """
    Save an uploaded PDF into the uploads folder.
    """

    if (file.content_type != "application/pdf" or not file.filename.lower().endswith(".pdf")):
        raise HTTPException (
            status_code=400,
            detail="Only PDF files are allowed."
        )
    UPLOAD_DIR.mkdir(exist_ok=True)

    destination = UPLOAD_DIR / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return destination


def extract_text(file):
    if (
        file.content_type != "application/pdf"
        or not file.filename.lower().endswith(".pdf")
    ):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    pdf = pymupdf.open(stream=file.file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text