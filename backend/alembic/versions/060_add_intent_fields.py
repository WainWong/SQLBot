"""add intent_answer field to chat_record

Revision ID: a1b2c3d4e5f6
Revises: db1a95567cbb
Create Date: 2025-01-14 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = 'db1a95567cbb'
branch_labels = None
depends_on = None


def upgrade():
    # 添加意图识别结果字段（JSON 格式存储）
    op.add_column('chat_record', sa.Column('intent_answer', sa.TEXT(), nullable=True))


def downgrade():
    op.drop_column('chat_record', 'intent_answer')
