from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 57")

@app.get("/")
def root():
    return {"message": "FastAPI Program 57", "docs": "/docs"}

# Run with: uvicorn main:app --reload
