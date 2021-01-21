"""empty message

Revision ID: 0ecba32a1175
Revises: 3f15960ee9e7
Create Date: 2021-01-20 09:07:22.697600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ecba32a1175'
down_revision = '3f15960ee9e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('interest', sa.Column('gender_interest', sa.Boolean(), nullable=False))
    op.create_unique_constraint(None, 'interest', ['dog_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'interest', type_='unique')
    op.drop_column('interest', 'gender_interest')
    # ### end Alembic commands ###