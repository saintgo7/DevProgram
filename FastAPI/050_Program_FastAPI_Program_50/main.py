from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 50")

@app.get("/")
def root():
    return {"message": "FastAPI Program 50", "docs": "/docs"}

# Run with: uvicorn main:app --reload
