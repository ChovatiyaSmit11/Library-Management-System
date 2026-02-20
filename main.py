from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import uvicorn
from handlers.student_handler import register_router
from handlers.book_handler import book_router
from handlers.search_handler import search_router
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

STATIC_FOLDER = Path("static")
STATIC_FOLDER.mkdir(parents=True, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('ALLOW_ORIGINS')],
    allow_credentials=os.getenv('ALLOW_CREDENTIALS'),
    allow_methods=[os.getenv('ALLOW_METHODS')],
    allow_headers=[os.getenv('ALLOW_HEADERS')],
)

app.include_router(register_router,  tags=['student'])
app.include_router(book_router, tags=['book'])
app.include_router(search_router, tags=['search'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
