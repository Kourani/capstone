

from app.models import db, Product, User, SCHEMA, environment
from sqlalchemy.sql import text

def seed_products():

    product0 = Product(
        shop_id=3, name='Scar', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/132464/pexels-photo-132464.jpeg"
    )
    product1= Product(
        shop_id=3, name='Simba', description='super soft and fluffy', category='toys', price=50.12, image="https://images.pexels.com/photos/207891/pexels-photo-207891.jpeg"
    )
    product2=Product(
        shop_id=3, name='Mufasa', description='awesome material', category='toys', price=5, image="https://images.pexels.com/photos/3068579/pexels-photo-3068579.jpeg"
    )
    product3 = Product(
        shop_id=3, name='Timon', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/139167/pexels-photo-139167.jpeg"
    )
    product4 = Product(
        shop_id=3, name='Pumbaa', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/1205650/pexels-photo-1205650.jpeg"
    )
    product5 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/1971084/pexels-photo-1971084.jpeg"
    )
    product6 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/1329328/pexels-photo-1329328.jpeg"
    )
    product7 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/1362595/pexels-photo-1362595.jpeg"
    )
    product8 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/3663060/pexels-photo-3663060.jpeg"
    )
    product9 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/2855628/pexels-photo-2855628.jpeg"
    )
    product10 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/1387014/pexels-photo-1387014.jpeg"
    )
    product11 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/6743164/pexels-photo-6743164.jpeg"
    )
    product12 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/590750/pexels-photo-590750.jpeg"
    )
    product13 = Product(
        shop_id=3, name='Rafiki', description='hand crafted', category='toys', price=29.99, image="https://images.pexels.com/photos/1364562/pexels-photo-1364562.jpeg"
    )
    product14 = Product(
        shop_id=4, name='The Testing', description='Use or be used to survive. School is not the same here one wrong answer is the difference between life and death. Choose wisely!', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1363452191i/13326831.jpg"
    )
    product15 = Product(
        shop_id=4, name='Scythe', description='Over population not a problem just normalize a career where if hired it is your job to kill. You decide who lives and who dies', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1456172676i/28954189.jpg"
    )
    product16 = Product(
        shop_id=4, name='WarCross', description="Some games you play others you surive. Can't get over the death of someone close, turn to AI", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1533058119i/41014903.jpg"
    )
    product17 = Product(
        shop_id=4, name='Cinder', description="A cyborg cinderella, well that's a twist to the original fairytale", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1507557775i/36381037.jpg"
    )
    product18 = Product(
        shop_id=4, name='The Program', description='Depression no problem lets just wipe those individuals clean', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1344986164i/11366397.jpg"
    )
    product19 = Product(
        shop_id=4, name='Genius', description='Secrecy smarts and a hunt well played', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1458765056i/25689033.jpg"
    )
    product20 = Product(
        shop_id=4, name='Legend', description='Justice or power you could only have one, choose', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1460224537i/29863662.jpg"
    )
    product21 = Product(
        shop_id=4, name='The 5th Wave', description='What are aliens but AI in disguise, can we coexist?', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1359853842i/16101128.jpg"
    )
    product22 = Product(
        shop_id=4, name='The Hunger Games', description="Poverty, Hunger, War no problem instill peace through fear. Kill or be killed that's the game", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1586722975i/2767052.jpg"
    )
    product23 = Product(
        shop_id=4, name='The 100', description="With thier hunger for improvements in tech, AI became too strong and humans have compromised the safety of Earth. To save the last of the human race, they move to space", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1377012321i/17332969.jpg"
    )
    product24 = Product(
        shop_id=4, name='Three Dark Crowns', description='Three sisters seperated at birth forced to kill each other against their will for a throne neither wants', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1469265712i/28374007.jpg"
    )
    product25 = Product(
        shop_id=4, name='Illuminae', description='Company gone astray, fraud, abuse and hidden scandals unraveled', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1443433956i/23395680.jpg"
    )
    product26 = Product(
        shop_id=4, name='Six of Crows', description="Mystery wit cleverness and street smarts that's what it takes to survive", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1651710803i/23437156.jpg"
    )
    product27 = Product(
        shop_id=4, name='Red Rising', description='Interplanatery War', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1461354651i/15839976.jpg"
    )
    product28 = Product(
        shop_id=4, name='An Ember in the Ashes', description='Deception lies and truth all wrapped in one', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1519425615i/27774758.jpg"
    )
    product29 = Product(
        shop_id=4, name='Aurora Rising', description='Space', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1560056657i/30075662.jpg"
    )
    product30 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/7992686/pexels-photo-7992686.jpeg"
    )
    product31 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/10983783/pexels-photo-10983783.jpeg"
    )
    product32 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/265906/pexels-photo-265906.jpeg"
    )
    product33 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/1413420/pexels-photo-1413420.jpeg"
    )
    product34 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/3266703/pexels-photo-3266703.jpeg"
    )
    product35 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/2697598/pexels-photo-2697598.jpeg"
    )
    product36 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/2697616/pexels-photo-2697616.jpeg"
    )
    product37 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595719/pexels-photo-4595719.jpeg"
    )
    product38 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/7250143/pexels-photo-7250143.png"
    )
    product39 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595723/pexels-photo-4595723.jpeg"
    )
    product40 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595727/pexels-photo-4595727.jpeg"
    )
    product41 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/11260679/pexels-photo-11260679.jpeg"
    )
    product42 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/47091/drill-milling-milling-machine-drilling-47091.jpeg"
    )
    product43 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/5974042/pexels-photo-5974042.jpeg"
    )
    product44 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/162553/keys-workshop-mechanic-tools-162553.jpeg"
    )
    product45 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/5691629/pexels-photo-5691629.jpeg"
    )
    product46 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/8780720/pexels-photo-8780720.jpeg"
    )
    product47 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/50691/drill-milling-milling-machine-drilling-50691.jpeg"
    )
    product48 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/3785929/pexels-photo-3785929.jpeg"
    )
    product49 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/414579/pexels-photo-414579.jpeg"
    )
    product50 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/3726313/pexels-photo-3726313.jpeg"
    )
    product51 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/4480453/pexels-photo-4480453.jpeg"
    )
    product52 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/5973896/pexels-photo-5973896.jpeg"
    )
    product53 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/2340698/pexels-photo-2340698.jpeg"
    )
    product54 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/3094042/pexels-photo-3094042.jpeg"
    )
    product55 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/1470008/pexels-photo-1470008.jpeg"
    )
    product56 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/2133982/pexels-photo-2133982.jpeg"
    )
    product57 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/4207892/pexels-photo-4207892.jpeg"
    )
    product58 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/11065506/pexels-photo-11065506.jpeg"
    )
    product59 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/10397360/pexels-photo-10397360.jpeg"
    )
    product60 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/6952058/pexels-photo-6952058.jpeg"
    )
    product61 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/6414823/pexels-photo-6414823.jpeg"
    )
    product62 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/7674538/pexels-photo-7674538.jpeg"
    )
    product63 = Product(
        shop_id=1, name='Rafiki', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/6694692/pexels-photo-6694692.jpeg"
    )
    product64 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/2113994/pexels-photo-2113994.jpeg"
    )
    product65 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg"
    )
    product66 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/280250/pexels-photo-280250.jpeg"
    )
    product67 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/3766111/pexels-photo-3766111.jpeg"
    )
    product68 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/2783873/pexels-photo-2783873.jpeg"
    )
    product69 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/3419331/pexels-photo-3419331.jpeg"
    )
    product70 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/125779/pexels-photo-125779.jpeg"
    )
    product71 = Product(
        shop_id=2, name='Rafiki', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/2799535/pexels-photo-2799535.jpeg"
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
    db.session.add(product64)
    db.session.add(product65)
    db.session.add(product66)
    db.session.add(product67)
    db.session.add(product68)
    db.session.add(product69)
    db.session.add(product70)
    db.session.add(product71)

    db.session.commit()

def undo_products():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
