from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 26")

@app.get("/")
def root():
    return {"message": "FastAPI Program 26", "docs": "/docs"}

# Run with: uvicorn main:app --reload
