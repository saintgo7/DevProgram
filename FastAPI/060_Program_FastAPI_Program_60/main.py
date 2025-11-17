from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 60")

@app.get("/")
def root():
    return {"message": "FastAPI Program 60", "docs": "/docs"}

# Run with: uvicorn main:app --reload
