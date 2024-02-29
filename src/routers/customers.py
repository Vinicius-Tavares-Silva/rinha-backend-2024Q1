from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.sql_app import crud, schemas
from src.sql_app.database import SessionLocal
from src.views.transaction_creator_view import TransactionCreatorView

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

@router.post('/{id}/transacoes', response_model=schemas.CustomerBase)
def create_transactions(
  id: str,
  transaction: schemas.TransactionCreate,
  db: Session = Depends(get_db)
):
  transaction_create_view = TransactionCreatorView()
  operation = transaction_create_view.validate_and_create(db, transaction, id)
  if operation['code'] == 200:
    return operation['data']
  raise HTTPException(status_code=operation['code'], detail=operation['data'])

@router.get('/{id}/extrato', response_model=schemas.Customer)
def read_statement(id: str, db: Session = Depends(get_db)):
  db_customer = crud.get_customer(db, id)
  return db_customer
