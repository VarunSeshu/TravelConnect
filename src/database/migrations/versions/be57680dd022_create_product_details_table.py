"""create product_details table

Revision ID: be57680dd022
Revises: d18d7bee6880
Create Date: 2022-01-13 21:27:20.421185

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'be57680dd022'
down_revision = 'd18d7bee6880'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_details',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('product_id', sa.BigInteger(), nullable=False),
    sa.Column('unit', sa.Enum('kg', 'gram', 'number', name='units'), nullable=True),
    sa.Column('actual_price', mysql.INTEGER(), nullable=True),
    sa.Column('discounted_price', mysql.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_details')
    # ### end Alembic commands ###
