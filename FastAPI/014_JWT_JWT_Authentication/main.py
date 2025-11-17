from fastapi import FastAPI

app = FastAPI(title="JWT Authentication")

@app.get("/")
def root():
    return {"message": "JWT Authentication", "docs": "/docs"}

# Run with: uvicorn main:app --reload
