from app.models import db, Shop, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_shops():
    shop0 = Shop(
        owner_id = 1, address='Farmington Hills', city='Grand Rapids', state='California', country='United States', name='Hand Crafts', currency='USD', image="https://images.pexels.com/photos/1705287/pexels-photo-1705287.jpeg")
    shop1 = Shop(
        owner_id = 2, address='BloomField', city='Lansing', state='Florida', country='United States', name='Remembered Gifts', currency='USD', image="https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg")
    shop2 = Shop(
        owner_id = 3, address='Gross Pointe', city='Detroit', state='Michigan', country='United States', name='Kid WonderLand', currency='USD', image="https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg")
    shop3 = Shop(
        owner_id = 1, address='6743 Nepal', city='Mumbai', state='Assam', country='India', name='A Thousand Lives', currency='Rupee', image="https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg")

    db.session.add(shop0)
    db.session.add(shop1)
    db.session.add(shop2)
    db.session.add(shop3)
    db.session.commit()


def undo_shops():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.shops RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM shops"))

    db.session.commit()
