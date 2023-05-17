"""empty message

Revision ID: 6010a4af0419
Revises: 
Create Date: 2023-05-16 10:25:10.783914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6010a4af0419'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_employees_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_employees_first_name'), ['first_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_employees_last_name'), ['last_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_employees_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_employees_username'))
        batch_op.drop_index(batch_op.f('ix_employees_last_name'))
        batch_op.drop_index(batch_op.f('ix_employees_first_name'))
        batch_op.drop_index(batch_op.f('ix_employees_email'))

    op.drop_table('employees')
    op.drop_table('roles')
    op.drop_table('departments')
    # ### end Alembic commands ###
