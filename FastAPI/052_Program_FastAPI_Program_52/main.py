from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 52")

@app.get("/")
def root():
    return {"message": "FastAPI Program 52", "docs": "/docs"}

# Run with: uvicorn main:app --reload
