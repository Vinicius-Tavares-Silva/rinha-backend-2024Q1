"""adjust datetime type

Revision ID: d491f39e71cf
Revises: 97d064eea522
Create Date: 2024-02-25 19:29:56.405914

"""
# pylint: disable-all
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd491f39e71cf'
down_revision: Union[str, None] = '97d064eea522'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('transactions')
    op.drop_table('customers')

    customers_table = op.create_table(
        'customers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('limit', sa.Integer),
        sa.Column('balance', sa.Integer),
    )

    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Integer),
        sa.Column('type', sa.String(1)),
        sa.Column('description', sa.String(200)),
        sa.Column('created_at', sa.DateTime),
        sa.Column('customer_id', sa.Integer),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'])
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
