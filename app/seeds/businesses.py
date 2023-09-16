from app.models import db, Business, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_businesses():
    business0 = Business(
        owner_id = 1, address='6743 Nepal', city='Nepal', state='India', country='India', language='bengali', currency='euro')
    business1 = Business(
        owner_id = 2, address='6743 Nepal', city='Nepal', state='India', country='India', language='bengali', currency='euro')
    business2 = Business(
        owner_id = 3, address='6743 Nepal', city='Nepal', state='India', country='India', language='bengali', currency='euro')

    db.session.add(business0)
    db.session.add(business1)
    db.session.add(business2)
    db.session.commit()


def undo_businesses():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.businesses RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM businesses"))

    db.session.commit()
