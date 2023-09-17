from flask.cli import AppGroup
from app.models.db import db, environment, SCHEMA

from .users import seed_users, undo_users
from .businesses import seed_businesses
from .orders import seed_orders
from .productComents import seed_productcomments
from .products import seed_products


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_productcomments()
        undo_businesses()
        undo_products()
        undo_orders()
    seed_users()
    seed_productcomments()
    seed_businesses()
    seed_products()
    seed_orders()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_productcomments()
    undo_businesses()
    undo_products()
    undo_orders()
    # Add other undo functions here
