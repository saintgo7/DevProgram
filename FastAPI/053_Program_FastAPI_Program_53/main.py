from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 53")

@app.get("/")
def root():
    return {"message": "FastAPI Program 53", "docs": "/docs"}

# Run with: uvicorn main:app --reload
