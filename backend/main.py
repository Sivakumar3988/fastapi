from fastapi import FastAPI

app = FastAPI(title="MyBlog",version="0.1.0")

@app.get("/")
def hello():
    return {"msg": "Hello FASTAPI"}
