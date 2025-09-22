from fastapi import FastApi
import os, httpx

app = FastApi(title="KidsApi Gateway")
USERS_URL = os.getenv("USERS_URL", "http://localhost:8001")

LESSONS_URL = os.getenv("LESSONS_URL", "http://localhost:8002")

@app.get("/")
def root():
    return {"message": "Вітаємо у KidsAPI!"}

@app.get("/users")
async def get_users():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{USERS_URL}/users")
        return r.json()

@app.post("/users")
async def add_user(user: dict):
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{USERS_URL}/users", json=user)
        return r.json()

@app.get("/lessons")
async def get_lessons():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{LESSONS_URL}/lessons")
        return r.json()