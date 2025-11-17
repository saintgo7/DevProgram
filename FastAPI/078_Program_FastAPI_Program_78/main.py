from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 78")

@app.get("/")
def root():
    return {"message": "FastAPI Program 78", "docs": "/docs"}

# Run with: uvicorn main:app --reload
