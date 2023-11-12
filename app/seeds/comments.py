
from app.models import db, User, Order, Comment, environment, SCHEMA
from sqlalchemy.sql import text

def seed_comments():
    Comment0 = Comment(
        comment="I've discovered my new favorite", user_id=1, product_id=1)
    Comment1 = Comment(
        comment='Love this, it tastes like home', user_id=2, product_id=1)
    Comment2 = Comment(
        comment='Nice and sweet must try', user_id=3, product_id=1)
    Comment3 = Comment(
        comment='Wow, simply amazing!', user_id=4, product_id=2)
    Comment4 = Comment(
        comment='I did not like it very much too sweet not crunchy enough', user_id=4, product_id=3)
    Comment5 = Comment(
        comment='Too sweet and jelly like for my liking', user_id=4, product_id=4)
    Comment6 = Comment(
        comment='Fantastic, will definitely come back for more', user_id=4, product_id=5)
    Comment7 = Comment(
        comment='Huh... almost like an upside down cheesecake but better!', user_id=4, product_id=6)
    Comment8 = Comment(
        comment='The memories, I used to eat these as a kid', user_id=4, product_id=7)
    Comment9 = Comment(
        comment="Oooh so aesthetic i'm hesitant to eat it", user_id=4, product_id=8)
    Comment10 = Comment(
        comment='I dont know how I feel about this, sorta like the tart flavor', user_id=4, product_id=9)

    db.session.add(Comment0)
    db.session.add(Comment1)
    db.session.add(Comment2)
    db.session.add(Comment3)
    db.session.add(Comment4)
    db.session.add(Comment5)
    db.session.add(Comment6)
    db.session.add(Comment7)
    db.session.add(Comment8)
    db.session.add(Comment9)
    db.session.add(Comment10)
    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
