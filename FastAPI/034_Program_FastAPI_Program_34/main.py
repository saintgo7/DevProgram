from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 34")

@app.get("/")
def root():
    return {"message": "FastAPI Program 34", "docs": "/docs"}

# Run with: uvicorn main:app --reload
