

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
        shop_id=3, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product15 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product16 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product17 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product18 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product19 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product20 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product21 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product22 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product23 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product24 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product25 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product26 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product27 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product28 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product29 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='books', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product30 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product31 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product32 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product33 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product34 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product35 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product36 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product37 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product38 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product39 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product40 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product41 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product42 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product43 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product44 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product45 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product46 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product47 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product48 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product49 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product50 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product51 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product52 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product53 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product54 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product55 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product56 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product57 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product58 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product59 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product60 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product61 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product62 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
    )
    product63 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg"
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
    db.session.add(product16)
    db.session.add(product17)
    db.session.add(product18)
    db.session.add(product19)
    db.session.add(product20)
    db.session.add(product21)
    db.session.add(product22)
    db.session.add(product23)
    db.session.add(product24)
    db.session.add(product25)
    db.session.add(product26)
    db.session.add(product27)
    db.session.add(product28)
    db.session.add(product29)
    db.session.add(product30)
    db.session.add(product31)
    db.session.add(product32)
    db.session.add(product33)
    db.session.add(product34)
    db.session.add(product35)
    db.session.add(product36)
    db.session.add(product37)
    db.session.add(product38)
    db.session.add(product39)
    db.session.add(product40)
    db.session.add(product41)
    db.session.add(product42)
    db.session.add(product43)
    db.session.add(product44)
    db.session.add(product45)
    db.session.add(product46)
    db.session.add(product47)
    db.session.add(product48)
    db.session.add(product49)
    db.session.add(product50)
    db.session.add(product51)
    db.session.add(product52)
    db.session.add(product53)
    db.session.add(product54)
    db.session.add(product55)
    db.session.add(product56)
    db.session.add(product57)
    db.session.add(product58)
    db.session.add(product59)
    db.session.add(product60)
    db.session.add(product61)
    db.session.add(product62)
    db.session.add(product63)


    db.session.commit()

def undo_products():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
