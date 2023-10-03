
from app.models import db, Favorite, environment, SCHEMA
from sqlalchemy.sql import text

def seed_favorites():
    Favorite0 = Favorite(
        user_id=1, category='Shop', number=1)
    Favorite1 = Favorite(
        user_id=1, category='Shop', number=2)

    db.session.add(Favorite0)
    db.session.add(Favorite1)
    db.session.commit()


def undo_favorites():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM favorites"))

    db.session.commit()
