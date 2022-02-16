"""create posts table

Revision ID: cebfd8afc0cc
Revises: 
Create Date: 2022-02-16 16:09:50.733307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cebfd8afc0cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column(
        'title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
