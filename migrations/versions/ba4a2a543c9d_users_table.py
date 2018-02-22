"""users table

Revision ID: ba4a2a543c9d
Revises: 780739b227a7
Create Date: 2018-02-21 12:04:03.606953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba4a2a543c9d'
down_revision = '780739b227a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_document_name'), 'document', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_document_name'), table_name='document')
    op.drop_table('document')
    # ### end Alembic commands ###
