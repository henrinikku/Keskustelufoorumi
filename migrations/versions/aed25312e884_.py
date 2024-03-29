"""empty message

Revision ID: aed25312e884
Revises: b2ae10115fa2
Create Date: 2020-10-03 14:10:02.467616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aed25312e884'
down_revision = 'b2ae10115fa2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('conversation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['Conversation.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Conversation', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Conversation', 'Category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Conversation', type_='foreignkey')
    op.drop_column('Conversation', 'category_id')
    op.drop_table('Message')
    # ### end Alembic commands ###
