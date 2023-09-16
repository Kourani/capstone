"""create products table

Revision ID: 3426e6af8039
Revises: a7d6836dc7d5
Create Date: 2023-09-16 12:18:30.151866

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '3426e6af8039'
down_revision = 'a7d6836dc7d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE products SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###