from app.models import db, User, ProductComment, environment, SCHEMA
from sqlalchemy.sql import text

def seed_productcomments():
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


def undo_productcomments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.productcomments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM productcomments"))

    db.session.commit()
