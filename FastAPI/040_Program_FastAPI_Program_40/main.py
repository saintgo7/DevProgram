from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 40")

@app.get("/")
def root():
    return {"message": "FastAPI Program 40", "docs": "/docs"}

# Run with: uvicorn main:app --reload
