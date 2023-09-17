from app.models import db, User, CommentA, environment, SCHEMA
from sqlalchemy.sql import text

def seed_commentas():
    Comment0 = CommentA(
        comment='love this, it tastes like home', item_quality=3)
    Comment1 = CommentA(
        comment='love this, it tastes like home', item_quality=3)
    Comment2 = CommentA(
        comment='love this, it tastes like home', item_quality=3)

    db.session.add(Comment0)
    db.session.add(Comment1)
    db.session.add(Comment2)
    db.session.commit()


def undo_commentas():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.commentas RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM commentas"))

    db.session.commit()
