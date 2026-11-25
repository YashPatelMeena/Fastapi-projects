"""add column to posts table

Revision ID: 8a1bf647f332
Revises: ed277cf5404a
Create Date: 2026-11-17 11:17:23.839687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a1bf647f332'
down_revision: Union[str, Sequence[str], None] = 'ed277cf5404a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
