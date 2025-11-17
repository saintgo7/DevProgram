from fastapi import FastAPI

app = FastAPI(title="SQLAlchemy Integration")

@app.get("/")
def root():
    return {"message": "SQLAlchemy Integration", "docs": "/docs"}

# Run with: uvicorn main:app --reload
