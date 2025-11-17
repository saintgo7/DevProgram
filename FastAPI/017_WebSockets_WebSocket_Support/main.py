from fastapi import FastAPI

app = FastAPI(title="WebSocket Support")

@app.get("/")
def root():
    return {"message": "WebSocket Support", "docs": "/docs"}

# Run with: uvicorn main:app --reload
