from http.client import HTTPException
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role

app = FastAPI()

#Simulating Database
db: List[User] =[
    User(
        id = uuid4(),
        first_name = "Diego",
        middle_name = "Andres",
        last_name = "Porres",
        gender = Gender.male,
        roles = [Role.admin],
    ),
    User(
        id = uuid4(),
        first_name = "Alex",
        middle_name = "James",
        last_name = "Jones",
        gender = Gender.male,
        roles = [Role.student],
    ),
    User(
        id = uuid4(),
        first_name = "Santiago",
        last_name = "Smith",
        gender = Gender.male,
        roles = [Role.teacher],
    )
]

# Root
@app.get("/")
def root():
    return {"Hello":"Mundo"}


#Get all users
@app.get("/api/v1/users")
async def fetch_users():
    return db;

#Add new user
@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id": user.id}

#Delete user
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"User with ID: {user_id} does not exist"
    )
