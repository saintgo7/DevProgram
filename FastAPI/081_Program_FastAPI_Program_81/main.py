from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 81")

@app.get("/")
def root():
    return {"message": "FastAPI Program 81", "docs": "/docs"}

# Run with: uvicorn main:app --reload
