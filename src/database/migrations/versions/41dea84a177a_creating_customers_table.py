"""creating customers  table

Revision ID: 41dea84a177a
Revises: f9377368e8f2
Create Date: 2022-01-13 20:48:13.395677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "41dea84a177a"
down_revision = "f9377368e8f2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "customers",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("home_address", sa.String(length=500), nullable=True),
        sa.Column("contact_no", sa.String(length=15), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("customers")
    # ### end Alembic commands ###
