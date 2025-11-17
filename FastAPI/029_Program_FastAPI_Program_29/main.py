from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 29")

@app.get("/")
def root():
    return {"message": "FastAPI Program 29", "docs": "/docs"}

# Run with: uvicorn main:app --reload
