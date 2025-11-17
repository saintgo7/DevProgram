from fastapi import FastAPI

app = FastAPI(title="Dependency Injection")

@app.get("/")
def root():
    return {"message": "Dependency Injection", "docs": "/docs"}

# Run with: uvicorn main:app --reload
