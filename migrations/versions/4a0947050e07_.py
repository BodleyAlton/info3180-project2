"""empty message

Revision ID: 4a0947050e07
Revises: ada10312c472
Create Date: 2017-04-17 15:37:43.245518

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4a0947050e07'
down_revision = 'ada10312c472'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wish_list', sa.Column('uid', sa.Integer(), nullable=False))
    op.drop_column('wish_list', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wish_list', sa.Column('id', mysql.INTEGER(display_width=11), nullable=False))
    op.drop_column('wish_list', 'uid')
    # ### end Alembic commands ###