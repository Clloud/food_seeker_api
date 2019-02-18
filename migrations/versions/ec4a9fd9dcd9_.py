"""empty message

Revision ID: ec4a9fd9dcd9
Revises: 13f22682473f
Create Date: 2019-02-18 17:38:25.859822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec4a9fd9dcd9'
down_revision = '13f22682473f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('canteen', sa.Column('update_time', sa.Integer(), nullable=True))
    op.add_column('canteen_image', sa.Column('update_time', sa.Integer(), nullable=True))
    op.add_column('food', sa.Column('update_time', sa.Integer(), nullable=True))
    op.add_column('food_image', sa.Column('update_time', sa.Integer(), nullable=True))
    op.add_column('image', sa.Column('update_time', sa.Integer(), nullable=True))
    op.add_column('restaurant', sa.Column('update_time', sa.Integer(), nullable=True))
    op.drop_constraint('restaurant_ibfk_1', 'restaurant', type_='foreignkey')
    op.create_foreign_key(None, 'restaurant', 'canteen', ['canteen_id'], ['id'])
    op.add_column('restaurant_image', sa.Column('update_time', sa.Integer(), nullable=True))
    op.add_column('review', sa.Column('update_time', sa.Integer(), nullable=True))
    op.add_column('review_image', sa.Column('update_time', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('update_time', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'update_time')
    op.drop_column('review_image', 'update_time')
    op.drop_column('review', 'update_time')
    op.drop_column('restaurant_image', 'update_time')
    op.drop_constraint(None, 'restaurant', type_='foreignkey')
    op.create_foreign_key('restaurant_ibfk_1', 'restaurant', 'restaurant', ['canteen_id'], ['id'])
    op.drop_column('restaurant', 'update_time')
    op.drop_column('image', 'update_time')
    op.drop_column('food_image', 'update_time')
    op.drop_column('food', 'update_time')
    op.drop_column('canteen_image', 'update_time')
    op.drop_column('canteen', 'update_time')
    # ### end Alembic commands ###
