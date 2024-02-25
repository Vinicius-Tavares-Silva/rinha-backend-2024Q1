import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Customer(Base):
  __tablename__ = "customers"

  id = Column(Integer, primary_key=True)
  limit = Column(Integer)
  balance = Column(Integer)

  transactions = relationship("Transaction", back_populates="customer")


class Transaction(Base):
  __tablename__ = "transactions"

  id = Column(Integer, primary_key=True)
  value = Column(Integer)
  type = Column(String)
  description = Column(String)
  created_at = Column(DateTime, default=datetime.datetime.utcnow())
  customer_id = Column(Integer, ForeignKey("customers.id"))

  customer = relationship("Customer", back_populates="transactions")
