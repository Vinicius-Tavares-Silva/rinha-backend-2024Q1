import datetime
from typing import List
from pydantic import BaseModel, Field


class TransactionBase(BaseModel):
  value: int = Field(..., alias='valor')
  type : str = Field(..., alias='tipo')
  description : str = Field(..., alias='descricao')

class TransactionCreate(TransactionBase):
  pass


class Transaction(TransactionBase):
  id: int
  customer_id: int
  created_at: datetime.datetime

  class Config:
    orm_mode = True


class CustomerBase(BaseModel):
  limit: int = Field(..., alias='limite')
  balance: int = Field(..., alias='saldo')

  class Config:
    allow_population_by_field_name = True


class CustomerCreate(CustomerBase):
  pass


class Customer(CustomerBase):
  id: int
  transactions: List[Transaction] = []

  class Config:
    orm_mode = True
