from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 97")

@app.get("/")
def root():
    return {"message": "FastAPI Program 97", "docs": "/docs"}

# Run with: uvicorn main:app --reload
