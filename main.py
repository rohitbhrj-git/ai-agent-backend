from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Welcome to my Api"}

@app.get("/posts")
def read_posts():
    return {"Hello": "Welcome to my Posts Api"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_posts": f"title: {payload['title']}, content: {payload['content']}"}