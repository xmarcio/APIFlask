"""empty message

Revision ID: 613ade24209c
Revises: 
Create Date: 2022-10-19 10:13:49.504790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '613ade24209c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curso',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('data_publicacao', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('curso')
    # ### end Alembic commands ###
