"""add last few columns to posts

Revision ID: 2625a5511e5b
Revises: f1d835b34209
Create Date: 2022-02-16 16:43:54.334355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2625a5511e5b'
down_revision = 'f1d835b34209'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
