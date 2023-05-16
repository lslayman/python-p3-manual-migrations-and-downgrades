"""Renaming students to scholars

Revision ID: b0c55313c42f
Revises: 791279dd0760
Create Date: 2023-05-15 18:30:51.611951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0c55313c42f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
