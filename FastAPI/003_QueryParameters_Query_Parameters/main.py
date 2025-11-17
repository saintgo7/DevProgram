from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

@app.get("/items/")
def read_items(
    skip: int = 0,
    limit: int = 10,
    q: Optional[str] = None
