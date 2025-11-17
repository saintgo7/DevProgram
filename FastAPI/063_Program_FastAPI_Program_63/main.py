from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 63")

@app.get("/")
def root():
    return {"message": "FastAPI Program 63", "docs": "/docs"}

# Run with: uvicorn main:app --reload
