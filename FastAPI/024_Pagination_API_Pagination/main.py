from fastapi import FastAPI

app = FastAPI(title="API Pagination")

@app.get("/")
def root():
    return {"message": "API Pagination", "docs": "/docs"}

# Run with: uvicorn main:app --reload
