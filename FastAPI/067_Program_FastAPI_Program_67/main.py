from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 67")

@app.get("/")
def root():
    return {"message": "FastAPI Program 67", "docs": "/docs"}

# Run with: uvicorn main:app --reload
