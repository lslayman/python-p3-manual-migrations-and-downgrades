"""Renaming email column to phone number

Revision ID: 2259832a05d8
Revises: 791279dd0760
Create Date: 2023-05-15 18:40:43.546230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2259832a05d8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='phone_number')


def downgrade() -> None:
    op.alter_column('students', 'phone_number', new_column_name='email')
