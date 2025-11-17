from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 48")

@app.get("/")
def root():
    return {"message": "FastAPI Program 48", "docs": "/docs"}

# Run with: uvicorn main:app --reload
