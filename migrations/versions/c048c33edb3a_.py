"""empty message

Revision ID: c048c33edb3a
Revises: 9b19ea1e56e2
Create Date: 2021-10-17 06:32:52.354509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c048c33edb3a'
down_revision = '9b19ea1e56e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('travel', sa.Column('travel_code', sa.String(127), nullable=True))
    op.execute("UPDATE travel SET travel_code = md5(random()::text) WHERE travel_code is NULL")
    op.alter_column("travel", "travel_code", nullable=False)
    op.drop_constraint('travel_code_key', 'travel', type_='unique')
    op.drop_constraint('travel_destination_key', 'travel', type_='unique')
    op.create_unique_constraint(None, 'travel', ['travel_code'])
    op.drop_column('travel', 'code')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('travel', sa.Column('code', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'travel', type_='unique')
    op.create_unique_constraint('travel_destination_key', 'travel', ['destination'])
    op.create_unique_constraint('travel_code_key', 'travel', ['code'])
    op.drop_column('travel', 'travel_code')
    # ### end Alembic commands ###