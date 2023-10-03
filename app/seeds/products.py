

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
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/7992686/pexels-photo-7992686.jpeg"
    )
    product31 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/10983783/pexels-photo-10983783.jpeg"
    )
    product32 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/265906/pexels-photo-265906.jpeg"
    )
    product33 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/1413420/pexels-photo-1413420.jpeg"
    )
    product34 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/3266703/pexels-photo-3266703.jpeg"
    )
    product35 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/2697598/pexels-photo-2697598.jpeg"
    )
    product36 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/2697616/pexels-photo-2697616.jpeg"
    )
    product37 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595719/pexels-photo-4595719.jpeg"
    )
    product38 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/7250143/pexels-photo-7250143.png"
    )
    product39 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595723/pexels-photo-4595723.jpeg"
    )
    product40 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595727/pexels-photo-4595727.jpeg"
    )
    product41 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/11260679/pexels-photo-11260679.jpeg"
    )
    product42 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/47091/drill-milling-milling-machine-drilling-47091.jpeg"
    )
    product43 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/5974042/pexels-photo-5974042.jpeg"
    )
    product44 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/162553/keys-workshop-mechanic-tools-162553.jpeg"
    )
    product45 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/5691629/pexels-photo-5691629.jpeg"
    )
    product46 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/8780720/pexels-photo-8780720.jpeg"
    )
    product47 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/50691/drill-milling-milling-machine-drilling-50691.jpeg"
    )
    product48 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/3785929/pexels-photo-3785929.jpeg"
    )
    product49 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/414579/pexels-photo-414579.jpeg"
    )
    product50 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/3726313/pexels-photo-3726313.jpeg"
    )
    product51 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/4480453/pexels-photo-4480453.jpeg"
    )
    product52 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/5973896/pexels-photo-5973896.jpeg"
    )
    product53 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/2340698/pexels-photo-2340698.jpeg"
    )
    product54 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/3094042/pexels-photo-3094042.jpeg"
    )
    product55 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/1470008/pexels-photo-1470008.jpeg"
    )
    product56 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/2133982/pexels-photo-2133982.jpeg"
    )
    product57 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/4207892/pexels-photo-4207892.jpeg"
    )
    product58 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/11065506/pexels-photo-11065506.jpeg"
    )
    product59 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/10397360/pexels-photo-10397360.jpeg"
    )
    product60 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/6952058/pexels-photo-6952058.jpeg"
    )
    product61 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/6414823/pexels-photo-6414823.jpeg"
    )
    product62 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/7674538/pexels-photo-7674538.jpeg"
    )
    product63 = Product(
        shop_id=0, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/6694692/pexels-photo-6694692.jpeg"
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
