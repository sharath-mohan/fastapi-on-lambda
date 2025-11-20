from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from mangum import Mangum

import httpx
results =[]

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    global results
    if not results:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://dummyjson.com/test?delay=500")
            results.append(response.json())
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": results}


handler = Mangum(app, lifespan="auto")

# def handler(event, context):
#     global results

#     response = httpx.get("https://jsonplaceholder.typicode.com/posts")
#     results = response.json()
          
#     asgi_handler = Mangum(app, lifespan="off")
#     return asgi_handler(event, context)