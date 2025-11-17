from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 98")

@app.get("/")
def root():
    return {"message": "FastAPI Program 98", "docs": "/docs"}

# Run with: uvicorn main:app --reload
