"""create owners table

Revision ID: d5896a63b63f
Revises: f496c8f91b24
Create Date: 2022-01-13 20:53:30.498487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d5896a63b63f"
down_revision = "f496c8f91b24"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "owners",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("home_address", sa.String(length=500), nullable=True),
        sa.Column("store_id", sa.BigInteger(), nullable=False),
        sa.Column("contact_no", sa.String(length=15), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["store_id"],
            ["stores.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("owners")
    # ### end Alembic commands ###
