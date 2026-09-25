from fastapi import FastAPI, HTTPException, status

from app.schema import UserCreate

app = FastAPI(title = "Lab 1 - FastAPI user API")

users:list[UserCreate] = []
@app.get("/health")
def health():
    return{"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "hello"}

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(new_user: UserCreate):
    for existing_user in users:
        if existing_user.user_id == new_user.user_id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="a user with this id already exists")
    users.append(new_user)
    return new_user

@app.get("/api/user")
def get_users():
    return users

@app.get("/api/user/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.user_id == user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

@app.delete("/api/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    global users
    users = [user for user in users if user.user_id != user_id]
    if user_id not in [user.user_id for user in users]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
