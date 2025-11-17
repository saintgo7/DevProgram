from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 88")

@app.get("/")
def root():
    return {"message": "FastAPI Program 88", "docs": "/docs"}

# Run with: uvicorn main:app --reload
