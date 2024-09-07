"""create post table

Revision ID: 0f5c2f8f9170
Revises: 
Create Date: 2024-09-07 16:22:27.103633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f5c2f8f9170'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable = False,primary_key = True),\
        sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
