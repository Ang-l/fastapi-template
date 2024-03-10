"""init

Revision ID: 7f5598f9c9aa
Revises: 
Create Date: 2024-03-10 06:47:09.602507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f5598f9c9aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backend',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='状态'),
    sa.Column('id', sa.Integer(), nullable=False, comment='id'),
    sa.Column('username', sa.String(length=50), nullable=True, comment='名称'),
    sa.Column('mobile', sa.String(length=11), nullable=True, comment='手机号'),
    sa.Column('password', sa.String(length=128), nullable=True, comment='密码'),
    sa.Column('is_active', sa.Boolean(), nullable=True, comment='状态'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_backend_id'), 'backend', ['id'], unique=False)
    op.create_index(op.f('ix_backend_mobile'), 'backend', ['mobile'], unique=True)
    op.create_table('users',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='状态'),
    sa.Column('id', sa.Integer(), nullable=False, comment='id'),
    sa.Column('username', sa.String(length=50), nullable=True, comment='名称'),
    sa.Column('mobile', sa.String(length=11), nullable=True, comment='手机号'),
    sa.Column('password', sa.String(length=128), nullable=True, comment='密码'),
    sa.Column('is_active', sa.Boolean(), nullable=True, comment='状态'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_mobile'), 'users', ['mobile'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_mobile'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_backend_mobile'), table_name='backend')
    op.drop_index(op.f('ix_backend_id'), table_name='backend')
    op.drop_table('backend')
    # ### end Alembic commands ###