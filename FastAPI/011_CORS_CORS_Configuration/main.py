from fastapi import FastAPI

app = FastAPI(title="CORS Configuration")

@app.get("/")
def root():
    return {"message": "CORS Configuration", "docs": "/docs"}

# Run with: uvicorn main:app --reload
