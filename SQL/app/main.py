from fastapi import FastAPI
from app.routers import user

app = FastAPI()

@app.get("/")
def root():
    return{"message": "FastAPI with MYSQL"}

# 라우터 등록
app.include_router(user.router)