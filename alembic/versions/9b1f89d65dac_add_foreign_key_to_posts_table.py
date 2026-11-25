"""add foreign key to posts table

Revision ID: 9b1f89d65dac
Revises: e17376af5421
Create Date: 2026-11-18 11:17:39.347707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b1f89d65dac'
down_revision: Union[str, Sequence[str], None] = 'e17376af5421'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable= False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete= 'CASCADE')
    
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name= 'posts')
    op.drop_column('posts', 'owner_id')
    pass
