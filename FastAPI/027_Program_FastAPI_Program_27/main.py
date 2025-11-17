from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 27")

@app.get("/")
def root():
    return {"message": "FastAPI Program 27", "docs": "/docs"}

# Run with: uvicorn main:app --reload
