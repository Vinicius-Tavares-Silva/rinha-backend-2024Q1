import datetime
from sqlalchemy.orm import Session

from ..sql_app import crud

class StatementReader:
  def __init__(self, db: Session):
    self.db = db

  def read(self, customer_id: int):
    statement = crud.get_statement(self.db, customer_id)
    if not statement['customer']:
      return None
    return self.__format_response(statement['customer'], statement['transactions'])


  def __format_response(self, customer: dict, transactions: list):
    return {
      'saldo': {
        'total': customer.balance,
        'data_extrato': datetime.datetime.now(),
        'limite': customer.limit
      },
      'ultimas_transacoes': transactions
    }
