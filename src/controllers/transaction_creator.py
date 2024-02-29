from sqlalchemy.orm import Session

from ..sql_app.schemas import TransactionCreate
from ..sql_app import crud

class TransactionCreator:
  def __init__(self, db: Session):
    self.db = db

  def create(self, transaction: TransactionCreate, customer_id: int):
    customer = crud.get_customer(self.db, customer_id)
    if not customer:
      return self.__format_response(None, None)

    if transaction.type == 'c':
      new_balance = customer.balance + transaction.value
      operation = crud.create_transaction(self.db, transaction, customer, new_balance)
      return self.__format_response(customer.id, operation)

    new_balance = customer.balance - transaction.value
    if self.__check_balance(new_balance, customer.limit):
      operation = crud.create_transaction(self.db, transaction, customer, new_balance)
      return self.__format_response(customer.id, operation)

    return self.__format_response(customer.id, None)

  def __check_balance(self, new_balance: int, limit: int):
    return new_balance >= (-1 * limit)

  def __format_response(self, customer_id: int, operation: dict):
    return {
        'customer_id': customer_id,
        'operation': operation
    }
