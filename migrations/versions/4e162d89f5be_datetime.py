"""Datetime

Revision ID: 4e162d89f5be
Revises: 4437dac8ecdf
Create Date: 2021-10-20 16:47:54.698989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e162d89f5be'
down_revision = '4437dac8ecdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('containers', 'tracking_code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('travel', 'travel_code',
               existing_type=sa.VARCHAR(length=127),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('travel', 'travel_code',
               existing_type=sa.VARCHAR(length=127),
               nullable=True)
    op.alter_column('containers', 'tracking_code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###