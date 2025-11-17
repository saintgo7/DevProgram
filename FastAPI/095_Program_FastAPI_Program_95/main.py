from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 95")

@app.get("/")
def root():
    return {"message": "FastAPI Program 95", "docs": "/docs"}

# Run with: uvicorn main:app --reload
