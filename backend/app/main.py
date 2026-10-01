from fastapi import FastAPI

app = FastAPI(
    title="AI Placement Intelligence API",
    description="Backend API for Resume and Skill Gap Analysis",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Placement Intelligence API is running!",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }