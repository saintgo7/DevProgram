from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 56")

@app.get("/")
def root():
    return {"message": "FastAPI Program 56", "docs": "/docs"}

# Run with: uvicorn main:app --reload
