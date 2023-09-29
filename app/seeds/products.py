

from app.models import db, Product, User, SCHEMA, environment
from sqlalchemy.sql import text

def seed_products():

    product0 = Product(
        shop_id=1, name='Scar', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product1= Product(
        shop_id=1, name='Simba', description='super soft and fluffy', category='toys', price=50.12, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product2=Product(
        shop_id=1, name='Mufasa', description='awesome material', category='toys', price=5, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product3 = Product(
        shop_id=1, name='Timon', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product4 = Product(
        shop_id=1, name='Pumbaa', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product5 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product6 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product7 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product8 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product9 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product10 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product11 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product12 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product13 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product14 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )

    db.session.add(product0)
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.add(product6)
    db.session.add(product7)
    db.session.add(product8)
    db.session.add(product9)
    db.session.add(product10)
    db.session.add(product11)
    db.session.add(product12)
    db.session.add(product13)
    db.session.add(product14)
    db.session.add(product15)

    db.session.commit()

def undo_products():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
