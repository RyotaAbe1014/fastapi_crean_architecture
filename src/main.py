from fastapi import FastAPI
from infrastructure.apis import user_apis

app = FastAPI()
app.include_router(user_apis.router)



@app.get("/")
def hello_world():
  return {"message": "hello world"}