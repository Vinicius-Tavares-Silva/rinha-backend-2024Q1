"""create customer table

Revision ID: ade19fbdb77b
Revises: 
Create Date: 2024-02-25 18:04:04.619791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ade19fbdb77b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('limit', sa.Integer),
        sa.Column('balance', sa.Integer),
    )


def downgrade() -> None:
    op.drop_table('customers')
