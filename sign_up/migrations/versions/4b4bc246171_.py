"""empty message

Revision ID: 4b4bc246171
Revises: 5930870a26b
Create Date: 2015-03-18 10:08:55.404885

"""

# revision identifiers, used by Alembic.
revision = '4b4bc246171'
down_revision = '5930870a26b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=60), nullable=False),
    sa.Column('token_id', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('customer')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=60), nullable=False),
    sa.Column('token_id', sa.VARCHAR(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('payment')
    ### end Alembic commands ###
