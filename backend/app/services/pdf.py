from pathlib import Path
import shutil

UPLOAD_DIR = Path("uploads")


def save_pdf(file):
    """
    Save an uploaded PDF into the uploads folder.
    """

    UPLOAD_DIR.mkdir(exist_ok=True)

    destination = UPLOAD_DIR / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return destination