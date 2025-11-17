from fastapi import FastAPI

app = FastAPI(title="Custom Middleware")

@app.get("/")
def root():
    return {"message": "Custom Middleware", "docs": "/docs"}

# Run with: uvicorn main:app --reload
