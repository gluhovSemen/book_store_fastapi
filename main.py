import uvicorn
from fastapi import FastAPI
from app import router as sales_router
app = FastAPI()


app.include_router(sales_router.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8001,)
