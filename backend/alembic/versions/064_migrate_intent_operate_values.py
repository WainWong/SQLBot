"""migrate intent operate values from 8,9 to 99,98

This migration updates the operate field in chat_log table for intent recognition
operations to avoid conflicts with upstream's new operation types (CHOOSE_TABLE='8',
FILTER_TERMS='9', etc.).

Revision ID: f7a8b9c0d1e2
Revises: c8751179a8de
Create Date: 2026-02-06

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f7a8b9c0d1e2'
down_revision = 'c8751179a8de'
branch_labels = None
depends_on = None


def upgrade():
    # Migrate RECOGNIZE_INTENT: '8' -> '99'
    op.execute("UPDATE chat_log SET operate = '99' WHERE operate = '8'")
    # Migrate GENERATE_CLARIFICATION: '9' -> '98'
    op.execute("UPDATE chat_log SET operate = '98' WHERE operate = '9'")


def downgrade():
    # Revert RECOGNIZE_INTENT: '99' -> '8'
    op.execute("UPDATE chat_log SET operate = '8' WHERE operate = '99'")
    # Revert GENERATE_CLARIFICATION: '98' -> '9'
    op.execute("UPDATE chat_log SET operate = '9' WHERE operate = '98'")