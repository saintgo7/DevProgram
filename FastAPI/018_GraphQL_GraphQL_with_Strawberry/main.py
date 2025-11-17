from fastapi import FastAPI

app = FastAPI(title="GraphQL with Strawberry")

@app.get("/")
def root():
    return {"message": "GraphQL with Strawberry", "docs": "/docs"}

# Run with: uvicorn main:app --reload
