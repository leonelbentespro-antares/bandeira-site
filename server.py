"""
Servidor estático simples para o site Bandeira Advogados.
Serve o index.html em qualquer rota — compatível com Railway.
"""
import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(docs_url=None, redoc_url=None)

BASE_DIR = Path(__file__).parent
HTML_FILE = BASE_DIR / "index.html"


@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=HTML_FILE.read_text(encoding="utf-8"))


@app.get("/{full_path:path}", response_class=HTMLResponse)
async def catch_all(full_path: str):
    return HTMLResponse(content=HTML_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("server:app", host="0.0.0.0", port=port)
