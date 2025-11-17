from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 69")

@app.get("/")
def root():
    return {"message": "FastAPI Program 69", "docs": "/docs"}

# Run with: uvicorn main:app --reload
