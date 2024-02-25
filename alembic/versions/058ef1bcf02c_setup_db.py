"""setup db

Revision ID: 058ef1bcf02c
Revises: ade19fbdb77b
Create Date: 2024-02-25 18:23:58.058555

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '058ef1bcf02c'
down_revision: Union[str, None] = 'ade19fbdb77b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Integer),
        sa.Column('type', sa.String(1)),
        sa.Column('description', sa.String(200)),
        sa.Column('customer_id', sa.Integer),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'])
    )

    customers_table = sa.table('customers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('limit', sa.Integer),
        sa.Column('balance', sa.Integer)
    )

    op.bulk_insert(customers_table,
    [
        {'id':1, 'limit':100000, 'balance':0},
        {'id':2, 'limit':80000, 'balance':0},
        {'id':3, 'limit':1000000, 'balance':0},
        {'id':4, 'limit':10000000, 'balance':0},
        {'id':5, 'limit':500000, 'balance':0},
    ]
)


def downgrade() -> None:
    op.drop_table('transactions')
    op.drop_table('customers')
