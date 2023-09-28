

from app.models import db, Product, User, SCHEMA, environment
from sqlalchemy.sql import text

def seed_products():

    product0 = Product(
        shop_id=1, name='Scar', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product1= Product(
        shop_id=2, name='Simba', description='super soft and fluffy', category='toys', price=50.12, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product2=Product(
        shop_id=3, name='Mufasa', description='awesome material', category='toys', price=5, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product3 = Product(
        shop_id=1, name='Timon', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product4 = Product(
        shop_id=1, name='Pumbaa', description='hand crafted', category='plush', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product5 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='plush', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )

    db.session.add(product0)
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.commit()

def undo_products():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
