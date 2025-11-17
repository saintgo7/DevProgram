from fastapi import FastAPI

app = FastAPI(title="HTTP Status Codes")

@app.get("/")
def root():
    return {"message": "HTTP Status Codes", "docs": "/docs"}

# Run with: uvicorn main:app --reload
