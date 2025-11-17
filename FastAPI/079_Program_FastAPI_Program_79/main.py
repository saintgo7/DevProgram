from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 79")

@app.get("/")
def root():
    return {"message": "FastAPI Program 79", "docs": "/docs"}

# Run with: uvicorn main:app --reload
