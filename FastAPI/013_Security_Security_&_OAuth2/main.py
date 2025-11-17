from fastapi import FastAPI

app = FastAPI(title="Security & OAuth2")

@app.get("/")
def root():
    return {"message": "Security & OAuth2", "docs": "/docs"}

# Run with: uvicorn main:app --reload
