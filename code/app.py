from code.config import TORTOISE_CONFIG
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Response, status
from tortoise import Tortoise


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(config=TORTOISE_CONFIG)
    yield
    await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)


@app.get('/health/')
async def health():
    return Response(status_code=status.HTTP_200_OK)


if __name__ == '__main__':
    uvicorn.run('code.app:app', host='0.0.0.0', port=8000, reload=True)
