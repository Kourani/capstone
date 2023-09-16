from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_businesses():
    business0 = Business(
        address='6743 Nepal', city='Nepal', state='India', country='India', language='bengali', currency='euro')
    business1 = Business(
        address='6743 Nepal', city='Nepal', state='India', country='India', language='bengali', currency='euro')
    business2 = Business(
        address='6743 Nepal', city='Nepal', state='India', country='India', language='bengali', currency='euro')

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
