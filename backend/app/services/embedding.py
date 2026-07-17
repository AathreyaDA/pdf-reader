import os

from dotenv import load_dotenv
from google import genai

import json
from pathlib import Path

load_dotenv()
OUTPUT_FILE = Path("embeddings.json")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def embed_text(text: str):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
    )

    return response.embeddings[0].values


def save_embeddings(chunks):
    data = []

    for chunk in chunks:
        vector = embed_text(chunk)

        data.append({
            "chunk": chunk,
            "embedding": vector
        })

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return data