from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 86")

@app.get("/")
def root():
    return {"message": "FastAPI Program 86", "docs": "/docs"}

# Run with: uvicorn main:app --reload
