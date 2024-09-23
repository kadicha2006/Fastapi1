"""empty message

Revision ID: c85dd6f9f849
Revises: a9118479f803
Create Date: 2024-09-21 10:03:34.186014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c85dd6f9f849'
down_revision: Union[str, None] = 'a9118479f803'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('total_number', sa.Integer(), nullable=False),
    sa.Column('buy_now', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category', sa.String(length=16), nullable=False),
    sa.Column('marka', sa.String(length=16), nullable=False),
    sa.Column('model', sa.String(length=16), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('year', sa.DateTime(), nullable=False),
    sa.Column('mileage', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=16), nullable=False),
    sa.Column('country', sa.String(length=16), nullable=False),
    sa.Column('with_photo', sa.Boolean(), nullable=False),
    sa.Column('color', sa.String(length=16), nullable=False),
    sa.Column('volume', sa.Float(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('product')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True)
    )
    op.drop_table('cars')
    op.drop_table('bets')
    # ### end Alembic commands ###
