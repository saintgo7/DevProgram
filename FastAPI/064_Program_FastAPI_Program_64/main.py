from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 64")

@app.get("/")
def root():
    return {"message": "FastAPI Program 64", "docs": "/docs"}

# Run with: uvicorn main:app --reload
