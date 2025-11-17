from fastapi import FastAPI

app = FastAPI(title="File Upload")

@app.get("/")
def root():
    return {"message": "File Upload", "docs": "/docs"}

# Run with: uvicorn main:app --reload
