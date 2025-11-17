from fastapi import FastAPI

app = FastAPI(title="Query Filtering")

@app.get("/")
def root():
    return {"message": "Query Filtering", "docs": "/docs"}

# Run with: uvicorn main:app --reload
