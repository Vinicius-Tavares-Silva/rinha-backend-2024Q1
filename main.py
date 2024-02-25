import uvicorn
from fastapi import FastAPI

from src.routers import customers
from src.sql_app import models
from src.sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customers.router)

if __name__ == "__main__":
  uvicorn.run(app, port=9999)
