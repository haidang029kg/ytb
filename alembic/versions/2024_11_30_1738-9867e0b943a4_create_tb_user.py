"""create tb user

Revision ID: 9867e0b943a4
Revises:
Create Date: 2024-11-30 17:38:15.143484

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9867e0b943a4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	pass


def downgrade() -> None:
	pass
