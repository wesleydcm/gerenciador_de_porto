"""empty message

Revision ID: 0dbaa814d0d0
Revises: 
Create Date: 2021-10-21 00:56:28.317565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dbaa814d0d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('harbor',
    sa.Column('id_harbor', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('country', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('teus', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_harbor'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=127), nullable=False),
    sa.PrimaryKeyConstraint('id_user'),
    sa.UniqueConstraint('username')
    )
    op.create_table('shipping_company',
    sa.Column('id_shipping_company', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('trading_name', sa.String(length=255), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_user'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id_shipping_company'),
    sa.UniqueConstraint('trading_name')
    )
    op.create_table('containers',
    sa.Column('id_container', sa.Integer(), nullable=False),
    sa.Column('tracking_code', sa.String(), nullable=True),
    sa.Column('teu', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('id_shipping_company', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_shipping_company'], ['shipping_company.id_shipping_company'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id_container'),
    sa.UniqueConstraint('tracking_code')
    )
    op.create_table('ships',
    sa.Column('id_ship', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('draught', sa.Integer(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('nationality', sa.String(length=50), nullable=False),
    sa.Column('id_shipping_company', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_shipping_company'], ['shipping_company.id_shipping_company'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id_ship'),
    sa.UniqueConstraint('name')
    )
    op.create_table('container_harbor',
    sa.Column('id_container_travel', sa.Integer(), nullable=False),
    sa.Column('entry_date', sa.DateTime(), nullable=False),
    sa.Column('exit_date', sa.DateTime(), nullable=True),
    sa.Column('id_container', sa.Integer(), nullable=True),
    sa.Column('id_harbor', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_container'], ['containers.id_container'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['id_harbor'], ['harbor.id_harbor'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id_container_travel')
    )
    op.create_table('ship_harbor',
    sa.Column('id_ship_harbor', sa.Integer(), nullable=False),
    sa.Column('entry_date', sa.DateTime(), nullable=True),
    sa.Column('exit_date', sa.DateTime(), nullable=True),
    sa.Column('id_ship', sa.Integer(), nullable=True),
    sa.Column('id_harbor', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_harbor'], ['harbor.id_harbor'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['id_ship'], ['ships.id_ship'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id_ship_harbor')
    )
    op.create_table('travel',
    sa.Column('id_travel', sa.Integer(), nullable=False),
    sa.Column('travel_code', sa.String(length=127), nullable=True),
    sa.Column('destination', sa.String(length=63), nullable=False),
    sa.Column('id_ship', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_ship'], ['ships.id_ship'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id_travel'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('destination')
    )
    op.create_table('container_travel',
    sa.Column('id_container_travel', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.Column('id_container', sa.Integer(), nullable=True),
    sa.Column('id_travel', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_container'], ['containers.id_container'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['id_travel'], ['travel.id_travel'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id_container_travel')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('container_travel')
    op.drop_table('travel')
    op.drop_table('ship_harbor')
    op.drop_table('container_harbor')
    op.drop_table('ships')
    op.drop_table('containers')
    op.drop_table('shipping_company')
    op.drop_table('users')
    op.drop_table('harbor')
    # ### end Alembic commands ###
