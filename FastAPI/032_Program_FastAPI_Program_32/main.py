from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 32")

@app.get("/")
def root():
    return {"message": "FastAPI Program 32", "docs": "/docs"}

# Run with: uvicorn main:app --reload
