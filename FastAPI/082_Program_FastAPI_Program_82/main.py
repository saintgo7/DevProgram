from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 82")

@app.get("/")
def root():
    return {"message": "FastAPI Program 82", "docs": "/docs"}

# Run with: uvicorn main:app --reload
