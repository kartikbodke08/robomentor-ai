from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.api.conversation import router as conversation_router

from app.core.init_db import init_db

init_db()

app = FastAPI(
    title = "RoboMentor AI",
    description="AI Learning companinon",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(conversation_router)


@app.get("/")
def root():
    return {"message":"RoboMentor Active"}

@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "service":"RoboMentor Backend"
    }

