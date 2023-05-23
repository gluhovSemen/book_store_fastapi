"""empty message

Revision ID: ab7368cf67ab
Revises: 2969690f9a5e
Create Date: 2023-05-23 14:22:53.116885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab7368cf67ab'
down_revision = '2969690f9a5e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sales',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_title', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('purchase_price', sa.Float(), nullable=True),
    sa.Column('purchase_quantity', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales')
    # ### end Alembic commands ###