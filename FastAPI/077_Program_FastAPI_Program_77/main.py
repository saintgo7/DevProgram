from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 77")

@app.get("/")
def root():
    return {"message": "FastAPI Program 77", "docs": "/docs"}

# Run with: uvicorn main:app --reload
