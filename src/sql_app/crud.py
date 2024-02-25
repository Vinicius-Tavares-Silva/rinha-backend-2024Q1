from sqlalchemy.orm import Session

from . import models, schemas


def get_customer(db: Session, customer_id: int):
  return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def create_transaction(db: Session, transaction: schemas.TransactionCreate, customer_id: int):
  db_transaction = models.Transaction(**transaction.model_dump(), customer_id = customer_id)
  db.add(db_transaction)
  db.commit()
  db.refresh(db_transaction)
  return db_transaction
