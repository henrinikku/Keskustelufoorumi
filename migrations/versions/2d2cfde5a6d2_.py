"""empty message

Revision ID: 2d2cfde5a6d2
Revises: f24df5b34fb0
Create Date: 2020-09-19 15:50:56.716059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d2cfde5a6d2'
down_revision = 'f24df5b34fb0'
branch_labels = None
depends_on = None


def upgrade():
    # Add admin user
    op.execute(
        """
        delete from public."User" where username = 'admin';
        insert into public."User" (
            created,
            updated,
            username,
            password,
            role
        ) values (
            now(),
            now(),
            'admin',
            'pbkdf2:sha256:150000$by4VNufi$c06ce9c25b64d8b1a2d50e13c7703a38460fd2c927c2256e19ac49e293831ace',
            'admin'
        );
        """
    )


def downgrade():
    pass
