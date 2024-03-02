from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import schemas
from .models import Customer, Transaction


def get_customer(db: Session, customer_id: int):
  return db.query(Customer).filter(Customer.id == customer_id).first()

def create_transaction(
  db: Session,
  transaction: schemas.TransactionCreate,
  customer: schemas.Customer,
  balance: int
):
  db_transaction = Transaction(**transaction.model_dump(), customer_id = customer.id)
  db.add(db_transaction)
  setattr(customer, 'balance', balance)
  db.commit()
  db.refresh(db_transaction)
  db.refresh(customer)
  return customer

def get_statement(db: Session, customer_id: int):
  customer = db.query(Customer).filter(Customer.id == customer_id).first()
  transactions = db.query(Transaction).filter(
    Transaction.customer_id == customer_id
  ).order_by(desc(Transaction.created_at)).limit(10)
  return {
    'customer': customer,
    'transactions': transactions
  }
