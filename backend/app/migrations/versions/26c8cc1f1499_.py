"""empty message

Revision ID: 26c8cc1f1499
Revises: 7f93842e6822
Create Date: 2020-11-16 08:59:52.448375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26c8cc1f1499'
down_revision = '7f93842e6822'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('devices_container_id_fkey', 'devices', type_='foreignkey')
    op.drop_column('devices', 'container_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('devices', sa.Column('container_id', sa.VARCHAR(length=32), autoincrement=False, nullable=True))
    op.create_foreign_key('devices_container_id_fkey', 'devices', 'containers', ['container_id'], ['id'])
    # ### end Alembic commands ###
