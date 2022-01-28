from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


dic={
    "fruit":["apple","banana"],
    "veg":['pea',"carrot"],
    "nonveg":["chicken","fish"]
}
class Tools:
    panels = ["fruit","veg","nonveg"]

@app.get("/",response_class =HTMLResponse)
async def root():
    return HTMLResponse("hello world")


@app.get("/dish/{name}")
async def dish(name):
    return dic.get(name)
