from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 83")

@app.get("/")
def root():
    return {"message": "FastAPI Program 83", "docs": "/docs"}

# Run with: uvicorn main:app --reload
