"""init_user_model

Revision ID: 07c71f4389b6
Revises:
Create Date: 2023-02-04 23:40:00.426237

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "07c71f4389b6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_model",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("email", sa.String(length=254), nullable=False),
        sa.Column("hashed_password", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "list_model",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("city", sa.String(length=100), nullable=True),
        sa.Column("list", sa.String(length=4000), nullable=True),
        sa.Column("phone", sa.String(length=100), nullable=True),
        sa.Column("service", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_model_email"), "user_model", ["email"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_model_email"), table_name="user_model")
    op.drop_table("user_model")
    op.drop_table("list_model")
    # ### end Alembic commands ###
