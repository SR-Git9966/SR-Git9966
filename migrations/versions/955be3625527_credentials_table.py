"""credentials table

Revision ID: 955be3625527
Revises: 
Create Date: 2022-08-01 23:16:59.884033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '955be3625527'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('credentials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_credentials_username'), 'credentials', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_credentials_username'), table_name='credentials')
    op.drop_table('credentials')
    # ### end Alembic commands ###
