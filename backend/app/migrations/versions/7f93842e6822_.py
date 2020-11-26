"""empty message

Revision ID: 7f93842e6822
Revises: 2bf54958732a
Create Date: 2020-11-16 07:38:09.825596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f93842e6822'
down_revision = '2bf54958732a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('devices', sa.Column('container_id', sa.String(length=32), nullable=True))
    op.create_foreign_key(None, 'devices', 'containers', ['container_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'devices', type_='foreignkey')
    op.drop_column('devices', 'container_id')
    # ### end Alembic commands ###