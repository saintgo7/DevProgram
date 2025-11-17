from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 39")

@app.get("/")
def root():
    return {"message": "FastAPI Program 39", "docs": "/docs"}

# Run with: uvicorn main:app --reload
