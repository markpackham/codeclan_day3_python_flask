"""posts table

Revision ID: 6162221900b0
Revises: 5d83b7db4576
Create Date: 2020-01-02 12:28:05.523056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6162221900b0'
down_revision = '5d83b7db4576'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('done', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'done')
    # ### end Alembic commands ###