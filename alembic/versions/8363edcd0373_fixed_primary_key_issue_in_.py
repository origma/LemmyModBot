"""fixed primary key issue in postphashhistory

Revision ID: 8363edcd0373
Revises: 027782211ee3
Create Date: 2023-11-28 15:37:19.879470

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8363edcd0373'
down_revision: Union[str, None] = '027782211ee3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post_phash_history', schema=None) as batch_op:
        batch_op.alter_column('community_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post_phash_history', schema=None) as batch_op:
        batch_op.alter_column('community_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
