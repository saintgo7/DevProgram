from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 54")

@app.get("/")
def root():
    return {"message": "FastAPI Program 54", "docs": "/docs"}

# Run with: uvicorn main:app --reload
