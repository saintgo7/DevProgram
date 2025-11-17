from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 44")

@app.get("/")
def root():
    return {"message": "FastAPI Program 44", "docs": "/docs"}

# Run with: uvicorn main:app --reload
