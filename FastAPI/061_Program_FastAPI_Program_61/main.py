from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 61")

@app.get("/")
def root():
    return {"message": "FastAPI Program 61", "docs": "/docs"}

# Run with: uvicorn main:app --reload
