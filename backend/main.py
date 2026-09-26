from fastapi import FastAPI

app = FastAPI(
    title="TajikGuide AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to TajikGuide AI"
    }
