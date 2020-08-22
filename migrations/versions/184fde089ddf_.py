"""empty message

Revision ID: 184fde089ddf
Revises: 
Create Date: 2020-08-22 17:20:18.537610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '184fde089ddf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lang_from', sa.String(length=16), nullable=True),
    sa.Column('lang_detected', sa.String(length=16), nullable=True),
    sa.Column('lang_to', sa.String(length=16), nullable=True),
    sa.Column('text_from', sa.Text(), nullable=True),
    sa.Column('text_to', sa.Text(), nullable=True),
    sa.Column('time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translation')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
