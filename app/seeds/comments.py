
from app.models import db, User, Order, Comment, environment, SCHEMA
from sqlalchemy.sql import text

def seed_comments():
    Comment0 = Comment(
        comment='love this, it tastes like homeeeeeeeeeeeeeeeeeeeeeeee', user_id=1, product_id=1)
    Comment1 = Comment(
        comment='love this, it tastes like home', user_id=2, product_id=1)
    Comment2 = Comment(
        comment='love this, it tastes like home', user_id=3, product_id=1)

    db.session.add(Comment0)
    db.session.add(Comment1)
    db.session.add(Comment2)
    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
