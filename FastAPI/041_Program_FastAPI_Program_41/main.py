from fastapi import FastAPI

app = FastAPI(title="FastAPI Program 41")

@app.get("/")
def root():
    return {"message": "FastAPI Program 41", "docs": "/docs"}

# Run with: uvicorn main:app --reload
