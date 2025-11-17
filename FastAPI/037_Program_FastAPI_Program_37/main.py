from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 37")

@app.get("/")
def root():
    return {"message": "FastAPI Program 37", "docs": "/docs"}

# Run with: uvicorn main:app --reload
