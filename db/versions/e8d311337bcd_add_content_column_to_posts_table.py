"""add content column to posts table

Revision ID: e8d311337bcd
Revises: 49d05b783b5e
Create Date: 2025-06-30 10:43:51.439788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8d311337bcd'
down_revision: Union[str, Sequence[str], None] = '49d05b783b5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
