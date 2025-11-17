from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 58")

@app.get("/")
def root():
    return {"message": "FastAPI Program 58", "docs": "/docs"}

# Run with: uvicorn main:app --reload
