from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 45")

@app.get("/")
def root():
    return {"message": "FastAPI Program 45", "docs": "/docs"}

# Run with: uvicorn main:app --reload
