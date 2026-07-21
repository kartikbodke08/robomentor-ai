from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
    title = "RoboMentor AI",
    description="AI Learning companinon",
    version="0.1.0"
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {"message":"RoboMentor Active"}

@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "service":"RoboMentor Backend"
    }

