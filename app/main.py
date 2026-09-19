from fastapi import FastAPI

app = FastAPI(title = "Lab 1 - FastAPI user API")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "hello"}