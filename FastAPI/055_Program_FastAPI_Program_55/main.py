from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 55")

@app.get("/")
def root():
    return {"message": "FastAPI Program 55", "docs": "/docs"}

# Run with: uvicorn main:app --reload
