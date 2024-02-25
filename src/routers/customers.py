from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.sql_app import crud, schemas
from src.sql_app.database import SessionLocal

router = APIRouter(
  prefix='/clientes',
  tags=['clientes']
)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.post('/{id}/transacoes', response_model=schemas.Transaction)
def create_transaction(
  id: str,
  transaction: schemas.TransactionCreate,
  db: Session = Depends(get_db)
):
  return crud.create_transaction(db, transaction, id)

@router.get('/{id}/extrato', response_model=schemas.Customer)
def read_statement(id: str, db: Session = Depends(get_db)):
  db_customer = crud.get_customer(db, id)
  return db_customer
