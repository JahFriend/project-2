"""empty message

Revision ID: 9fbb01b67c1d
Revises: 09eb13326353
Create Date: 2019-04-23 19:23:12.864215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fbb01b67c1d'
down_revision = '09eb13326353'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=60), nullable=True),
    sa.Column('biography', sa.Text(), nullable=False),
    sa.Column('profile_photo', sa.String(length=20), nullable=True),
    sa.Column('joined_on', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('caption', sa.Text(), nullable=True),
    sa.Column('created_on', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('username', name='users_username_key')
    )
    op.drop_table('post')
    op.drop_table('user')
    # ### end Alembic commands ###