from app.models import db, Shop, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_shops():
    shop0 = Shop(
        owner_id = 1, address='6743 Nepal', city='Nepal', state='India', country='India', name='bengali', currency='euro', image="https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg")
    shop1 = Shop(
        owner_id = 2, address='6743 Nepal', city='Nepal', state='India', country='India', name='bengali', currency='euro', image="https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg")
    shop2 = Shop(
        owner_id = 3, address='6743 Nepal', city='Nepal', state='India', country='India', name='bengali', currency='euro', image="https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg")

    db.session.add(shop0)
    db.session.add(shop1)
    db.session.add(shop2)
    db.session.commit()


def undo_shops():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.shops RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM shops"))

    db.session.commit()
