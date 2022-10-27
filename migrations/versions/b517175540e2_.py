"""empty message

Revision ID: b517175540e2
Revises: 8982e17d656b
Create Date: 2022-10-26 09:25:31.687096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b517175540e2'
down_revision = '8982e17d656b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('api_key', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'api_key')
    # ### end Alembic commands ###
