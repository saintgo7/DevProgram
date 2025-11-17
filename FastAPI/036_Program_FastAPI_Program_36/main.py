from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 36")

@app.get("/")
def root():
    return {"message": "FastAPI Program 36", "docs": "/docs"}

# Run with: uvicorn main:app --reload
