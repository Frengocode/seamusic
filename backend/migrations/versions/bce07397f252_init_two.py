"""init two

Revision ID: bce07397f252
Revises: e8c488a0d130
Create Date: 2023-11-20 17:31:26.416242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bce07397f252'
down_revision: Union[str, None] = 'e8c488a0d130'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('music')
    op.drop_table('author')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('author',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nickname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], name='author_user_fkey'),
    sa.PrimaryKeyConstraint('id', name='author_pkey')
    )
    op.create_table('music',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='music_pkey')
    )
    # ### end Alembic commands ###