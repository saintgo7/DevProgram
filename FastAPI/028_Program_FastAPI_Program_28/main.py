from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 28")

@app.get("/")
def root():
    return {"message": "FastAPI Program 28", "docs": "/docs"}

# Run with: uvicorn main:app --reload
