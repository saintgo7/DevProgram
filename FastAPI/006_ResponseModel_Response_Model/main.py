from fastapi import FastAPI

app = FastAPI(title="Response Model")

@app.get("/")
def root():
    return {"message": "Response Model", "docs": "/docs"}

# Run with: uvicorn main:app --reload
