from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 47")

@app.get("/")
def root():
    return {"message": "FastAPI Program 47", "docs": "/docs"}

# Run with: uvicorn main:app --reload
