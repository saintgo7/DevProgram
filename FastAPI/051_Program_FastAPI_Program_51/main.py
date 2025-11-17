from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 51")

@app.get("/")
def root():
    return {"message": "FastAPI Program 51", "docs": "/docs"}

# Run with: uvicorn main:app --reload
