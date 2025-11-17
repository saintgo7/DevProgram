from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 84")

@app.get("/")
def root():
    return {"message": "FastAPI Program 84", "docs": "/docs"}

# Run with: uvicorn main:app --reload
