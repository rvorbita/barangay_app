"""register table

Revision ID: 601ec71a0364
Revises: 
Create Date: 2021-01-28 17:31:36.246764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '601ec71a0364'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('register',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=100), nullable=True),
    sa.Column('lastname', sa.String(length=100), nullable=True),
    sa.Column('middlename', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('mobile', sa.Integer(), nullable=True),
    sa.Column('alias', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile')
    )
    op.create_index(op.f('ix_register_alias'), 'register', ['alias'], unique=True)
    op.create_index(op.f('ix_register_email'), 'register', ['email'], unique=True)
    op.create_index(op.f('ix_register_firstname'), 'register', ['firstname'], unique=True)
    op.create_index(op.f('ix_register_lastname'), 'register', ['lastname'], unique=True)
    op.create_index(op.f('ix_register_middlename'), 'register', ['middlename'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_register_middlename'), table_name='register')
    op.drop_index(op.f('ix_register_lastname'), table_name='register')
    op.drop_index(op.f('ix_register_firstname'), table_name='register')
    op.drop_index(op.f('ix_register_email'), table_name='register')
    op.drop_index(op.f('ix_register_alias'), table_name='register')
    op.drop_table('register')
    # ### end Alembic commands ###
