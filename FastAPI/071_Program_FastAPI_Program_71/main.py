from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 71")

@app.get("/")
def root():
    return {"message": "FastAPI Program 71", "docs": "/docs"}

# Run with: uvicorn main:app --reload
