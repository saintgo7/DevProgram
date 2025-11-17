from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 93")

@app.get("/")
def root():
    return {"message": "FastAPI Program 93", "docs": "/docs"}

# Run with: uvicorn main:app --reload
