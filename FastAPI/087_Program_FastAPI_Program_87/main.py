from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 87")

@app.get("/")
def root():
    return {"message": "FastAPI Program 87", "docs": "/docs"}

# Run with: uvicorn main:app --reload
