from fastapi import FastAPI

app = FastAPI(title="Custom Serializers")

@app.get("/")
def root():
    return {"message": "Custom Serializers", "docs": "/docs"}

# Run with: uvicorn main:app --reload
