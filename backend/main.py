from fastapi import FastAPI
from places import get_places

app = FastAPI(
    title="TajikGuide AI",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to TajikGuide AI!"
    }

@app.get("/places")
def places():
    return get_places()
