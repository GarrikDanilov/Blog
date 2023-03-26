"""add tag

Revision ID: cd8df8b2e7d0
Revises: 3fb2a337beaa
Create Date: 2023-03-25 11:07:41.940525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd8df8b2e7d0'
down_revision = '3fb2a337beaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tag'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=120), server_default='', nullable=False),
    sa.Column('last_name', sa.String(length=120), server_default='', nullable=False),
    sa.Column('email', sa.String(length=255), server_default='', nullable=False),
    sa.Column('is_staff', sa.Boolean(), nullable=False),
    sa.Column('_password', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_author_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_author'))
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=200), server_default='', nullable=False),
    sa.Column('body', sa.Text(), server_default='', nullable=False),
    sa.Column('dt_created', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('dt_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], name=op.f('fk_article_author_id_author')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_article'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    op.drop_table('author')
    op.drop_table('user')
    op.drop_table('tag')
    # ### end Alembic commands ###
