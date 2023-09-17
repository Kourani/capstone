

from app.models import db, Product, User, SCHEMA, environment
from sqlalchemy.sql import text

def seed_products():

    product0 = Product(
        shop_id=1, name='teddy bear', category='plush', price=29.99
    )
    product1= Product(
        shop_id=2, name='Scar', category='toys', price=50.12
    )
    product2=Product(
        shop_id=3, name='Squish', category='stress relif', price=5
    )

    db.session.add(product0)
    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()

def undo_products():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
