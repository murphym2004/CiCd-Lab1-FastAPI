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
        if existing_user.user_id == new_user.new_id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="a user with this id already exists")
    users.append(new_user)
    return new_user

@app.get("/api/user")
def get_users():
    return users
