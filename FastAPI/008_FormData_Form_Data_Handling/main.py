from fastapi import FastAPI

app = FastAPI(title="Form Data Handling")

@app.get("/")
def root():
    return {"message": "Form Data Handling", "docs": "/docs"}

# Run with: uvicorn main:app --reload
