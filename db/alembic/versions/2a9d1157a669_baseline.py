"""baseline

Revision ID: 2a9d1157a669
Revises: 
Create Date: 2020-05-18 22:58:27.913996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a9d1157a669'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'headline',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('added', sa.DateTime(), default=sa.func.now()),
        sa.Column('language', sa.String()),
        sa.Column('original_text', sa.String()),
        sa.Column('translated_text', sa.String())
    )


def downgrade():
    op.drop_table('headline')
