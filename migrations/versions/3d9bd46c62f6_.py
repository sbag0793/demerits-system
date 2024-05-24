"""empty message

Revision ID: 3d9bd46c62f6
Revises: e67a1455c341
Create Date: 2024-05-24 11:01:48.298612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d9bd46c62f6'
down_revision = 'e67a1455c341'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('score_board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('p_point', sa.Integer(), nullable=True),
    sa.Column('n_point', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['student.id'], name=op.f('fk_score_board_id_student'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_score_board'))
    )
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('positive', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('negative', sa.Boolean(), nullable=True))
        batch_op.drop_column('Type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Type', sa.VARCHAR(length=10), nullable=False))
        batch_op.drop_column('negative')
        batch_op.drop_column('positive')

    op.drop_table('score_board')
    # ### end Alembic commands ###
