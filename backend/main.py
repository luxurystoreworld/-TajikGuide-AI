from fastapi import FastAPI
from places import router as places_router

app = FastAPI(
    title="TajikGuide AI",
    version="1.0.0"
)

app.include_router(places_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to TajikGuide AI"
    }
