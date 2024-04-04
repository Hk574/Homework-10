"""first migration

Revision ID: 7e8c0f36de08
Revises: 
Create Date: 2024-04-04 04:21:56.999268

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e8c0f36de08'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('profile_picture_url', sa.String(length=255), nullable=True),
    sa.Column('last_login_at', sa.DateTime(), nullable=True),
    sa.Column('failed_login_attempts', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('events',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('is_public', sa.Boolean(), nullable=True),
    sa.Column('creator_id', sa.UUID(), nullable=False),
    sa.Column('qr_code_path', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_roles',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_approvals',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('event_id', sa.UUID(), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('approval_reason', sa.Text(), nullable=True),
    sa.Column('rejection_reason', sa.Text(), nullable=True),
    sa.Column('reviewed_by_id', sa.UUID(), nullable=True),
    sa.Column('reviewed_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['reviewed_by_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_reviews',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('event_id', sa.UUID(), nullable=False),
    sa.Column('reviewer_id', sa.UUID(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['reviewer_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_sections',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('event_id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('registration_deadline', sa.DateTime(), nullable=True),
    sa.Column('additional_info', sa.Text(), nullable=True),
    sa.Column('qr_code_path', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_tags',
    sa.Column('event_id', sa.UUID(), nullable=False),
    sa.Column('tag_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('event_id', 'tag_id')
    )
    op.create_table('event_registrations',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('section_id', sa.UUID(), nullable=False),
    sa.Column('registered_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['section_id'], ['event_sections.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_registrations')
    op.drop_table('event_tags')
    op.drop_table('event_sections')
    op.drop_table('event_reviews')
    op.drop_table('event_approvals')
    op.drop_table('user_roles')
    op.drop_table('events')
    op.drop_table('users')
    op.drop_table('tags')
    # ### end Alembic commands ###