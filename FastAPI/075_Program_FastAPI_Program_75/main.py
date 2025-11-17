from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 75")

@app.get("/")
def root():
    return {"message": "FastAPI Program 75", "docs": "/docs"}

# Run with: uvicorn main:app --reload
