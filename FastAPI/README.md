# FastAPI Programs

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
