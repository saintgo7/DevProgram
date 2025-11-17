from fastapi import FastAPI

app = FastAPI(title="Advanced Validation")

@app.get("/")
def root():
    return {"message": "Advanced Validation", "docs": "/docs"}

# Run with: uvicorn main:app --reload
