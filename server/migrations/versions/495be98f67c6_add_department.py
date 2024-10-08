"""add Department

Revision ID: 495be98f67c6
Revises: 529462888a78
Create Date: 2024-10-02 19:27:35.784669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '495be98f67c6'
down_revision = '529462888a78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
