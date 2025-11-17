from fastapi import FastAPI

app = FastAPI(title="Background Tasks")

@app.get("/")
def root():
    return {"message": "Background Tasks", "docs": "/docs"}

# Run with: uvicorn main:app --reload
