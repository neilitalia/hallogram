"""empty message

<<<<<<< HEAD:migrations/versions/9546e77d9106_.py
Revision ID: 9546e77d9106
Revises: 
Create Date: 2021-10-07 18:30:36.439431
=======
Revision ID: 5e36e8528488
Revises: 
Create Date: 2021-10-07 19:30:26.860647
>>>>>>> 3debc0ab67a37843e64bb42f04c8bb952447de48:migrations/versions/5e36e8528488_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<< HEAD:migrations/versions/9546e77d9106_.py
revision = '9546e77d9106'
=======
revision = '5e36e8528488'
>>>>>>> 3debc0ab67a37843e64bb42f04c8bb952447de48:migrations/versions/5e36e8528488_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('tip_jar', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('costume', sa.String(length=255), nullable=False),
    sa.Column('claps', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('users')
    # ### end Alembic commands ###