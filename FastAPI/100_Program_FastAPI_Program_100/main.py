from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 100")

@app.get("/")
def root():
    return {"message": "FastAPI Program 100", "docs": "/docs"}

# Run with: uvicorn main:app --reload
