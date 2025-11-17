from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 43")

@app.get("/")
def root():
    return {"message": "FastAPI Program 43", "docs": "/docs"}

# Run with: uvicorn main:app --reload
