from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 59")

@app.get("/")
def root():
    return {"message": "FastAPI Program 59", "docs": "/docs"}

# Run with: uvicorn main:app --reload
