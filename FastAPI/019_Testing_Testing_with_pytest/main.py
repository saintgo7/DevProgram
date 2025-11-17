from fastapi import FastAPI

app = FastAPI(title="Testing with pytest")

@app.get("/")
def root():
    return {"message": "Testing with pytest", "docs": "/docs"}

# Run with: uvicorn main:app --reload
