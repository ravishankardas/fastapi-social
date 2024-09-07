"""add content column to post table

Revision ID: 55b8404edd61
Revises: 0f5c2f8f9170
Create Date: 2024-09-07 16:49:03.102483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55b8404edd61'
down_revision = '0f5c2f8f9170'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
