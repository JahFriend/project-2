"""empty message

Revision ID: 4b5678e1b50e
Revises: 48cd3bf53e83
Create Date: 2019-04-23 19:57:18.697073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b5678e1b50e'
down_revision = '48cd3bf53e83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('follower_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], name='follows_follower_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='follows_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='follows_pkey')
    )
    # ### end Alembic commands ###
