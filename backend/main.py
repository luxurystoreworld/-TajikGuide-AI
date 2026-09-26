from fastapi import FastAPI, HTTPException
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

@app.get("/places/{name}")
def place(name: str):
    for place in get_places():
        if place["name"].lower() == name.lower():
            return place

    raise HTTPException(
        status_code=404,
        detail="Place not found"
    )
