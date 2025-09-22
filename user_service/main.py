import DB
from fastapi import FastApi, FastAPI
from pydantic import BaseModel

app = FastAPI(title="Users Service")
class User(BaseModel):
    name: str
    age: int
    DB = []
@app.get("/users")
def list_users():
    return DB
@app.post("/users", status_code=201)
def create_user(user: User):
    DB.append(user)
    return user