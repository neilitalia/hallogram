"""empty message

Revision ID: ffa66a355784
Revises: 90971f628468
Create Date: 2021-10-07 17:21:01.393763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffa66a355784'
down_revision = '90971f628468'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('tip_jar', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'tip_jar')
    # ### end Alembic commands ###
