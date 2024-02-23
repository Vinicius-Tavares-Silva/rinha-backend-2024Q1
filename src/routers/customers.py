from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
  prefix='/clientes',
  tags=['clientes']
)

class Transaction(BaseModel):
  valor: int
  tipo : str
  descricao : str

@router.post('/{id}/transacoes')
async def create_transaction(id: str, transaction: Transaction):
  return {
    'id': id,
    'limite': 1000,
    'saldo': 1000 - transaction.valor
  }

@router.get('/{id}/extrato')
async def read_statement(id: str):
  return { 'extrato': id }
