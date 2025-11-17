from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 94")

@app.get("/")
def root():
    return {"message": "FastAPI Program 94", "docs": "/docs"}

# Run with: uvicorn main:app --reload
