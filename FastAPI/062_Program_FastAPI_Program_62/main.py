from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 62")

@app.get("/")
def root():
    return {"message": "FastAPI Program 62", "docs": "/docs"}

# Run with: uvicorn main:app --reload
