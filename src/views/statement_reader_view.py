from sqlalchemy.orm import Session
from ..controllers.statement_reader import StatementReader

class StatementReaderView:

  def validate_and_read(self, db: Session, customer_id: int):
    statement_reader = StatementReader(db)
    response = statement_reader.read(customer_id)
    if not response:
      return {'code': 404,'data': {'balance': None, 'limit': None}}
    return {'code': 200, 'data': response}
    