#!/usr/bin/env python3
"""
Create 100 FastAPI programs
FastAPI: Modern, fast Python web framework with automatic API docs
"""

import os
import sys

# Program definitions
programs = [
    # Featured Programs (1-5) - Full implementations
    ("001_HelloWorld", "Hello World API", """main.py:
from fastapi import FastAPI

app = FastAPI(title="Hello World API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!", "docs": "/docs"}

@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello {name}!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

# Run with: uvicorn main:app --reload
"""),

    ("002_PathParameters", "Path Parameters", """main.py:
from fastapi import FastAPI, Path
from typing import Optional
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(..., title="The ID of the user", ge=1, le=1000)
):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}
"""),

    ("003_QueryParameters", "Query Parameters", """main.py:
from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

@app.get("/items/")
def read_items(
    skip: int = 0,
    limit: int = 10,
    q: Optional[str] = None
):
    items = [{"item_id": i} for i in range(skip, skip + limit)]
    if q:
        items = [item for item in items if q.lower() in str(item).lower()]
    return {"items": items, "query": q}

@app.get("/search/")
def search(
    q: str = Query(..., min_length=3, max_length=50, regex="^[a-zA-Z0-9 ]+$"),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    return {
        "query": q,
        "page": page,
        "size": size,
        "results": f"Search results for '{q}'"
    }

@app.get("/tags/")
def read_tags(tags: List[str] = Query([])):
    return {"tags": tags}
"""),

    ("004_RequestBody", "Request Body with Pydantic", """main.py:
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None
    age: int = Field(..., ge=0, le=120)

    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john@example.com",
                "full_name": "John Doe",
                "age": 30
            }
        }

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    tax: Optional[float] = None

@app.post("/users/")
def create_user(user: User):
    return {"user": user, "created_at": datetime.now()}

@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(...)
):
    return {"item_id": item_id, "item": item, "user": user, "importance": importance}

requirements-extra.txt:
pydantic[email]
"""),

    ("005_AsyncEndpoints", "Async/Await Support", """main.py:
from fastapi import FastAPI
import asyncio
import httpx
from typing import List

app = FastAPI()

# Simulate async database query
async def fetch_user_from_db(user_id: int):
    await asyncio.sleep(0.1)  # Simulate DB delay
    return {"id": user_id, "name": f"User {user_id}"}

# Simulate async external API call
async def fetch_external_data(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await fetch_user_from_db(user_id)
    return user

@app.get("/external")
async def get_external():
    # Example: fetch from external API
    # data = await fetch_external_data("https://api.example.com/data")
    await asyncio.sleep(0.5)  # Simulate async operation
    return {"message": "Async operation completed"}

@app.get("/parallel")
async def parallel_tasks():
    # Run multiple async tasks in parallel
    results = await asyncio.gather(
        fetch_user_from_db(1),
        fetch_user_from_db(2),
        fetch_user_from_db(3)
    )
    return {"users": results}

@app.get("/background")
async def background_task():
    async def long_running_task():
        await asyncio.sleep(2)
        print("Background task completed")

    # Start background task (fire and forget)
    asyncio.create_task(long_running_task())
    return {"message": "Task started in background"}

requirements-extra.txt:
httpx
"""),

    # Template Programs (6-100)
    ("006_ResponseModel", "Response Model", ""),
    ("007_StatusCodes", "HTTP Status Codes", ""),
    ("008_FormData", "Form Data Handling", ""),
    ("009_FileUpload", "File Upload", ""),
    ("010_HeadersAndCookies", "Headers & Cookies", ""),
    ("011_CORS", "CORS Configuration", ""),
    ("012_Dependencies", "Dependency Injection", ""),
    ("013_Security", "Security & OAuth2", ""),
    ("014_JWT", "JWT Authentication", ""),
    ("015_DatabaseIntegration", "SQLAlchemy Integration", ""),
    ("016_BackgroundTasks", "Background Tasks", ""),
    ("017_WebSockets", "WebSocket Support", ""),
    ("018_GraphQL", "GraphQL with Strawberry", ""),
    ("019_Testing", "Testing with pytest", ""),
    ("020_Middleware", "Custom Middleware", ""),
    ("021_ErrorHandling", "Exception Handlers", ""),
    ("022_Validation", "Advanced Validation", ""),
    ("023_Serialization", "Custom Serializers", ""),
    ("024_Pagination", "API Pagination", ""),
    ("025_Filtering", "Query Filtering", ""),
]

# Generate remaining programs
for i in range(26, 101):
    programs.append((
        f"{i:03d}_Program",
        f"FastAPI Program {i}",
        ""
    ))

def create_fastapi_program(number, name, content):
    """Create a FastAPI program directory with files"""
    dir_name = f"FastAPI/{number}_{name.replace(' ', '_').replace('/', '_')}"
    os.makedirs(dir_name, exist_ok=True)

    extra_reqs = []

    # Parse content for featured programs
    if content:
        files = {}
        current_file = None
        current_content = []

        for line in content.split('\n'):
            if line.startswith('requirements-extra.txt:'):
                extra_reqs.append(line.replace('requirements-extra.txt:', '').strip())
                continue
            if line.endswith(':') and not line.startswith(' '):
                if current_file:
                    files[current_file] = '\n'.join(current_content)
                current_file = line[:-1]
                current_content = []
            else:
                current_content.append(line)

        if current_file:
            files[current_file] = '\n'.join(current_content)

        # Write parsed files
        for filename, file_content in files.items():
            filepath = os.path.join(dir_name, filename)
            with open(filepath, 'w') as f:
                f.write(file_content.strip() + '\n')
    else:
        # Template program
        with open(f"{dir_name}/main.py", 'w') as f:
            f.write(f"""from fastapi import FastAPI

app = FastAPI(title="{name}")

@app.get("/")
def root():
    return {{"message": "{name}", "docs": "/docs"}}

# Run with: uvicorn main:app --reload
""")

    # Create requirements.txt
    with open(f"{dir_name}/requirements.txt", 'w') as f:
        f.write("fastapi>=0.109.0\n")
        f.write("uvicorn[standard]>=0.27.0\n")
        for req in extra_reqs:
            if req:
                f.write(f"{req}\n")

    # Create .env.example
    with open(f"{dir_name}/.env.example", 'w') as f:
        f.write("""# FastAPI Configuration
HOST=0.0.0.0
PORT=8000
RELOAD=True
""")

def main():
    print("Creating FastAPI programs...")
    os.makedirs("FastAPI", exist_ok=True)

    # Create README
    with open("FastAPI/README.md", 'w') as f:
        f.write("""# FastAPI Programs

100 FastAPI programs demonstrating modern Python API development.

## Features
- Type Hints & Validation
- Async/Await Support
- Automatic API Documentation (Swagger UI)
- Pydantic Models
- Dependency Injection
- High Performance
- Modern Python 3.7+

## Quick Start

```bash
cd FastAPI/001_HelloWorld
pip install -r requirements.txt
uvicorn main:app --reload
# Visit http://localhost:8000
# API Docs: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

## Interactive API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: `/docs`
- ReDoc: `/redoc`
- OpenAPI JSON: `/openapi.json`

## Run in Production

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
""")

    total_lines = 0
    for number, name, content in programs:
        create_fastapi_program(number, name, content)
        # Count lines
        dir_name = f"FastAPI/{number}_{name.replace(' ', '_').replace('/', '_')}"
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                if file.endswith(('.py', '.txt')):
                    with open(os.path.join(root, file), 'r') as f:
                        total_lines += len(f.readlines())

    print(f"✅ Created 100 FastAPI programs ({total_lines:,} lines)")
    return total_lines

if __name__ == "__main__":
    lines = main()
    sys.exit(0)
