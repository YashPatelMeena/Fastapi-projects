"""add last few columns to posts table

Revision ID: 5bcb98edf056
Revises: 9b1f89d65dac
Create Date: 2026-11-18 11:51:39.232030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bcb98edf056'
down_revision: Union[str, Sequence[str], None] = '9b1f89d65dac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable= False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone= True), server_default= sa.text('now()'), nullable= False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
