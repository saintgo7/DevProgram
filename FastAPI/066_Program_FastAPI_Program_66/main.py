from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 66")

@app.get("/")
def root():
    return {"message": "FastAPI Program 66", "docs": "/docs"}

# Run with: uvicorn main:app --reload
