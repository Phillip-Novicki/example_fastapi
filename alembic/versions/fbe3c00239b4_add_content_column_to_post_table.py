"""add content column to post table

Revision ID: fbe3c00239b4
Revises: cebfd8afc0cc
Create Date: 2022-02-16 16:21:47.401489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbe3c00239b4'
down_revision = 'cebfd8afc0cc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
