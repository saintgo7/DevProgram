from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 89")

@app.get("/")
def root():
    return {"message": "FastAPI Program 89", "docs": "/docs"}

# Run with: uvicorn main:app --reload
