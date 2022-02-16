"""add user table

Revision ID: 10d1bae78ba4
Revises: fbe3c00239b4
Create Date: 2022-02-16 16:26:02.724476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10d1bae78ba4'
down_revision = 'fbe3c00239b4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                        server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
