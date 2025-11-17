from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 92")

@app.get("/")
def root():
    return {"message": "FastAPI Program 92", "docs": "/docs"}

# Run with: uvicorn main:app --reload
