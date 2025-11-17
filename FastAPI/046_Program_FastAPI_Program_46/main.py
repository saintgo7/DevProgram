from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 46")

@app.get("/")
def root():
    return {"message": "FastAPI Program 46", "docs": "/docs"}

# Run with: uvicorn main:app --reload
