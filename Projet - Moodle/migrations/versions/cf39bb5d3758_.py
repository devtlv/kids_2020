"""empty message

Revision ID: cf39bb5d3758
Revises: e9d0f9b65542
Create Date: 2020-07-06 19:08:41.500402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf39bb5d3758'
down_revision = 'e9d0f9b65542'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commentaire',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contenu', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('exercice_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['exercice_id'], ['exercice.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('commentaire')
    # ### end Alembic commands ###
