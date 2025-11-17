from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 33")

@app.get("/")
def root():
    return {"message": "FastAPI Program 33", "docs": "/docs"}

# Run with: uvicorn main:app --reload
