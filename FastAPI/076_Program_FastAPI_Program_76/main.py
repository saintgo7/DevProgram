from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 76")

@app.get("/")
def root():
    return {"message": "FastAPI Program 76", "docs": "/docs"}

# Run with: uvicorn main:app --reload
