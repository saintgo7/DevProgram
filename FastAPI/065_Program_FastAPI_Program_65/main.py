from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 65")

@app.get("/")
def root():
    return {"message": "FastAPI Program 65", "docs": "/docs"}

# Run with: uvicorn main:app --reload
