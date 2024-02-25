import datetime
from typing import List
from pydantic import BaseModel


class TransactionBase(BaseModel):
  value: int
  type : str
  description : str

class TransactionCreate(TransactionBase):
  pass


class Transaction(TransactionBase):
  id: int
  customer_id: int
  created_at: datetime.datetime

  class Config:
    orm_mode = True


class CustomerBase(BaseModel):
  limit: int
  balance: int


class CustomerCreate(CustomerBase):
  pass


class Customer(CustomerBase):
  id: int
  transactions: List[Transaction] = []

  class Config:
    orm_mode = True
