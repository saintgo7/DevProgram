from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 68")

@app.get("/")
def root():
    return {"message": "FastAPI Program 68", "docs": "/docs"}

# Run with: uvicorn main:app --reload
