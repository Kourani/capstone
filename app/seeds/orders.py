from app.models import db, User, Order, environment, SCHEMA
from sqlalchemy.sql import text

def seed_orders():
    order0 = Order(
        status='delivered')
    order1 = Order(
        status='on the way')
    order2 = Order(
        status='still at facility')

    db.session.add(order0)
    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()


def undo_productComments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM orders"))

    db.session.commit()
