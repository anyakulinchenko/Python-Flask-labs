"""empty message

Revision ID: 2926bf01c762
Revises: 
Create Date: 2020-12-07 16:40:00.276137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2926bf01c762'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=30), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=40), nullable=True),
    sa.Column('total_rating', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('sid')
    )
    op.create_table('teachers',
    sa.Column('tid', sa.Integer(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=30), nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=30), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=40), nullable=True),
    sa.PrimaryKeyConstraint('tid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers')
    op.drop_table('students')
    # ### end Alembic commands ###
