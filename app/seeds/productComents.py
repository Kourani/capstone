from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_productComments():
    productComment0 = ProductComment(
        comment='love this, it tastes like home', item_quality=3)
    productComment1 = ProductComment(
        comment='love this, it tastes like home', item_quality=3)
    productComment2 = ProductComment(
        comment='love this, it tastes like home', item_quality=3)

    db.session.add(productComment0)
    db.session.add(productComment1)
    db.session.add(productComment2)
    db.session.commit()


def undo_productComments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.productComments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM productComments"))

    db.session.commit()