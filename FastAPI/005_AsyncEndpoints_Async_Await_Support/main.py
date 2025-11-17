from fastapi import FastAPI
import asyncio
import httpx
from typing import List

app = FastAPI()

# Simulate async database query
