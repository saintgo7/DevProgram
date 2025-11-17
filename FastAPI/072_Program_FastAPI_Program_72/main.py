from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 72")

@app.get("/")
def root():
    return {"message": "FastAPI Program 72", "docs": "/docs"}

# Run with: uvicorn main:app --reload
