from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 31")

@app.get("/")
def root():
    return {"message": "FastAPI Program 31", "docs": "/docs"}

# Run with: uvicorn main:app --reload
