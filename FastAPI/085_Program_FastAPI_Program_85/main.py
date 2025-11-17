from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 85")

@app.get("/")
def root():
    return {"message": "FastAPI Program 85", "docs": "/docs"}

# Run with: uvicorn main:app --reload
