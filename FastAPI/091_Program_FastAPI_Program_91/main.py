from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 91")

@app.get("/")
def root():
    return {"message": "FastAPI Program 91", "docs": "/docs"}

# Run with: uvicorn main:app --reload
