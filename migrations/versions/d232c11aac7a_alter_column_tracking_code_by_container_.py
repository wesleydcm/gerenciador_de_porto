"""alter column tracking_code by container_modelel

Revision ID: d232c11aac7a
Revises: d931207705a8
Create Date: 2021-10-19 12:40:38.915799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd232c11aac7a'
down_revision = 'd931207705a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('travel', 'travel_code',
               existing_type=sa.VARCHAR(length=127),
               nullable=True)
    op.alter_column('containers', 'tracking_code',
               existing_type=sa.VARCHAR(length=127),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('travel', 'travel_code',
               existing_type=sa.VARCHAR(length=127),
               nullable=True)
    # ### end Alembic commands ###
