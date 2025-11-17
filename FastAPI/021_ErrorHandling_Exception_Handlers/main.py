from fastapi import FastAPI

app = FastAPI(title="Exception Handlers")

@app.get("/")
def root():
    return {"message": "Exception Handlers", "docs": "/docs"}

# Run with: uvicorn main:app --reload
