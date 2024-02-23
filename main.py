from fastapi import FastAPI
import uvicorn

from src.routers import customers

app = FastAPI()

app.include_router(customers.router)

if __name__ == "__main__":
  uvicorn.run(app, port=9999)
