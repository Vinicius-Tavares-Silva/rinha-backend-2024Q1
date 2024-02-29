from sqlalchemy.orm import Session
from ..sql_app.schemas import TransactionCreate
from ..controllers.transaction_creator import TransactionCreator

class TransactionCreatorView:

  def validate_and_create(self, db: Session, transaction: TransactionCreate, customer_id: int):
    transaction_create = TransactionCreator(db)
    response = transaction_create.create(transaction, customer_id)
    if not response['customer_id']:
      return {'code': 404,'data': {'balance': None, 'limit': None}}
    if not response['operation']:
      return {'code': 422, 'data': {'balance': None, 'limit': None}}

    return {'code': 200, 'data': response['operation']}
    