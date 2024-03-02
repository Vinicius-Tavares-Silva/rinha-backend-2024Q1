import datetime
from typing import Dict, List, Union
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

class StatementTransaction(BaseModel):
  value: int = Field(..., serialization_alias='valor')
  type : str = Field(..., serialization_alias='tipo')
  description : str = Field(..., serialization_alias='descricao')
  created_at: datetime.datetime = Field(..., serialization_alias='realizada_em')


class CustomerBase(BaseModel):
  limit: int = Field(..., serialization_alias='limite')
  balance: int = Field(..., serialization_alias='saldo')

  class Config:
    allow_population_by_field_name = True


class CustomerCreate(CustomerBase):
  pass


class Customer(CustomerBase):
  id: int
  transactions: List[Transaction] = []

  class Config:
    orm_mode = True


class StatementBase(BaseModel):
  saldo: Dict[str, Union[str, int, datetime.datetime]]

  class Config:
    orm_mode = True


class Statement(StatementBase):
  ultimas_transacoes: List[StatementTransaction] = []

  class Config:
    orm_mode = True
