from fastapi import FastAPI

app = FastAPI(title="Headers & Cookies")

@app.get("/")
def root():
    return {"message": "Headers & Cookies", "docs": "/docs"}

# Run with: uvicorn main:app --reload
