from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestModel(BaseModel):
    key: str

@app.get("/api/test")
async def get_test():
    return "Hello World"


@app.post("/api/test")
async def post_test(data: RequestModel):
    if data.key == "cxcxc" :
        return  "Succeeded"

    else:
        return  "Failed"


