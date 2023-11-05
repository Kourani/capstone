

from app.models import db, Product, User, SCHEMA, environment
from sqlalchemy.sql import text

def seed_products():

    product0 = Product(
        shop_id=3, name='Ladyfingers', description='exquisite light and airy biscuits with a crispy crunch', category='sweets', price=29.99, image="https://images.pexels.com/photos/7803117/pexels-photo-7803117.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product1= Product(
        shop_id=3, name='Baklava', description='sweet and syrupy with a soft crunch', category='sweets', price=50.12, image="https://images.pexels.com/photos/5323489/pexels-photo-5323489.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product2=Product(
        shop_id=3, name='Baklava', description='Buttery flaky and stuffed with nuts. rich nutty flavor', category='sweets', price=5, image="https://images.pexels.com/photos/17255931/pexels-photo-17255931/free-photo-of-close-up-of-slices-of-baklava.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300",image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product3 = Product(
        shop_id=3, name='Turkish Delight', description='Sweet and chewy confection. Very sweet and sugary with a soft and chewy texture', category='sweets', price=29.99, image="https://images.pexels.com/photos/6161509/pexels-photo-6161509.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300",image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product4 = Product(
        shop_id=3, name='Baklava', description='Pistachio stuffed with hard outer shell. Super crunchy', category='sweets', price=29.99, image="https://images.pexels.com/photos/17255923/pexels-photo-17255923/free-photo-of-close-up-of-kadayif-baklava.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product5 = Product(
        shop_id=3, name='Kunafa', description='Sweet and syrupy almost like a cheesecake but richer in flavor', category='sweets', price=29.99, image="https://images.pexels.com/photos/11833316/pexels-photo-11833316.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product6 = Product(
        shop_id=3, name='Pudding', description='hand crafted', category='sweets', price=29.99, image="https://images.pexels.com/photos/3547176/pexels-photo-3547176.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product7 = Product(
        shop_id=3, name='Macron', description='hand crafted', category='sweets', price=29.99, image="https://images.pexels.com/photos/7474290/pexels-photo-7474290.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product8 = Product(
        shop_id=3, name='Berry Blast', description='hand crafted', category='sweets', price=29.99, image="https://images.pexels.com/photos/2693447/pexels-photo-2693447.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product9 = Product(
        shop_id=3, name='Choclate Eclair', description='hand crafted', category='sweets', price=29.99, image="https://images.pexels.com/photos/5945568/pexels-photo-5945568.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product10 = Product(
        shop_id=3, name='Assortment Variety', description='hand crafted', category='sweets', price=29.99, image="https://images.pexels.com/photos/4913389/pexels-photo-4913389.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product11 = Product(
        shop_id=3, name='Pistachio layered Ice Cream', description='hand crafted', category='sweets', price=29.99, image="https://images.pexels.com/photos/13020802/pexels-photo-13020802.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product12 = Product(
        shop_id=3, name='Nuts Cream and Choclate', description='hand crafted', category='sweets', price=29.99, image="https://images.pexels.com/photos/7783241/pexels-photo-7783241.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product13 = Product(
        shop_id=3, name='Pudding', description='hand crafted', category='sweets', price=29.99, image="https://images.pexels.com/photos/3026810/pexels-photo-3026810.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product14 = Product(
        shop_id=4, name='The Testing', description='Use or be used to survive. School is not the same here one wrong answer is the difference between life and death. Choose wisely!', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1363452191i/13326831.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product15 = Product(
        shop_id=4, name='Scythe', description='Over population not a problem just normalize a career where if hired it is your job to kill. You decide who lives and who dies', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1456172676i/28954189.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product16 = Product(
        shop_id=4, name='WarCross', description="Some games you play others you surive. Can't get over the death of someone close, turn to AI", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1533058119i/41014903.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product17 = Product(
        shop_id=4, name='Cinder', description="A cyborg cinderella, well that's a twist to the original fairytale", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1507557775i/36381037.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product18 = Product(
        shop_id=4, name='The Program', description='Depression no problem lets just wipe those individuals clean', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1344986164i/11366397.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product19 = Product(
        shop_id=4, name='Genius', description='Secrecy smarts and a hunt well played', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1458765056i/25689033.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product20 = Product(
        shop_id=4, name='Legend', description='Justice or power you could only have one, choose', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1460224537i/29863662.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product21 = Product(
        shop_id=4, name='The 5th Wave', description='What are aliens but AI in disguise, can we coexist?', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1359853842i/16101128.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product22 = Product(
        shop_id=4, name='The Hunger Games', description="Poverty, Hunger, War no problem instill peace through fear. Kill or be killed that's the game", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1586722975i/2767052.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product23 = Product(
        shop_id=4, name='The 100', description="With thier hunger for improvements in tech, AI became too strong and humans have compromised the safety of Earth. To save the last of the human race, they move to space", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1377012321i/17332969.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product24 = Product(
        shop_id=4, name='Three Dark Crowns', description='Three sisters seperated at birth forced to kill each other against their will for a throne neither wants', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1469265712i/28374007.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product25 = Product(
        shop_id=4, name='Illuminae', description='Company gone astray, fraud, abuse and hidden scandals unraveled', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1443433956i/23395680.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product26 = Product(
        shop_id=4, name='Six of Crows', description="Mystery wit cleverness and street smarts that's what it takes to survive", category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1651710803i/23437156.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product27 = Product(
        shop_id=4, name='Red Rising', description='Interplanatery War', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1461354651i/15839976.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product28 = Product(
        shop_id=4, name='An Ember in the Ashes', description='Deception lies and truth all wrapped in one', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1519425615i/27774758.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product29 = Product(
        shop_id=4, name='Aurora Rising', description='Space', category='books', price=29.99, image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1560056657i/30075662.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product30 = Product(
        shop_id=2, name='Golden Thin Bangles', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/7992686/pexels-photo-7992686.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product31 = Product(
        shop_id=2, name='Rose Gold Diamond Earnings', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/10983783/pexels-photo-10983783.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product32 = Product(
        shop_id=2, name='Embedded Diamonds', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/265906/pexels-photo-265906.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product33 = Product(
        shop_id=2, name='Feathery Earings', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/1413420/pexels-photo-1413420.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product34 = Product(
        shop_id=2, name='Sterling Silver Ring', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/3266703/pexels-photo-3266703.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product35 = Product(
        shop_id=2, name='Blue Topaz Sliver', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/2697598/pexels-photo-2697598.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product36 = Product(
        shop_id=2, name='Cubed Sterling Silver necklace', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/2697616/pexels-photo-2697616.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product37 = Product(
        shop_id=2, name='Diamond Embeded necklace', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595719/pexels-photo-4595719.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product38 = Product(
        shop_id=2, name='Gold attached heart necklace', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/7250143/pexels-photo-7250143.png?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product39 = Product(
        shop_id=2, name='Exotic shaped gold necklace', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595723/pexels-photo-4595723.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product40 = Product(
        shop_id=2, name='Gold hollow heart necklace', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595727/pexels-photo-4595727.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product41 = Product(
        shop_id=2, name='Gold beaded bracelet', description='hand crafted', category='jewelry', price=29.99, image="https://images.pexels.com/photos/11260679/pexels-photo-11260679.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product42 = Product(
        shop_id=1, name='Spiral Drill Tip', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/47091/drill-milling-milling-machine-drilling-47091.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product43 = Product(
        shop_id=1, name='Drilling Machine', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/5974042/pexels-photo-5974042.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product44 = Product(
        shop_id=1, name='Compelete Wrench Set', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/162553/keys-workshop-mechanic-tools-162553.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product45 = Product(
        shop_id=1, name='Wrench', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/5691629/pexels-photo-5691629.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product46 = Product(
        shop_id=1, name='Nuts and Bolts', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/8780720/pexels-photo-8780720.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product47 = Product(
        shop_id=1, name='Drill Tip', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/50691/drill-milling-milling-machine-drilling-50691.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product48 = Product(
        shop_id=1, name='Gears', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/3785929/pexels-photo-3785929.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product49 = Product(
        shop_id=1, name='Gear Set', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/414579/pexels-photo-414579.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product50 = Product(
        shop_id=1, name='Barometer', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/3726313/pexels-photo-3726313.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product51 = Product(
        shop_id=1, name='Tool Box Set', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/4480453/pexels-photo-4480453.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product52 = Product(
        shop_id=1, name='Chisel Set', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/5973896/pexels-photo-5973896.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product53 = Product(
        shop_id=1, name='Bowls for two', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/2340698/pexels-photo-2340698.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product54 = Product(
        shop_id=1, name='Coffee Cups', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/3094042/pexels-photo-3094042.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product55 = Product(
        shop_id=1, name='Tea Set', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/1470008/pexels-photo-1470008.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product56 = Product(
        shop_id=1, name='Tea Set', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/2133982/pexels-photo-2133982.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product57 = Product(
        shop_id=1, name='Vase', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/4207892/pexels-photo-4207892.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product58 = Product(
        shop_id=1, name='Dinner Set', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/11065506/pexels-photo-11065506.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product59 = Product(
        shop_id=1, name='Tea Set', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/10397360/pexels-photo-10397360.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product60 = Product(
        shop_id=1, name='Soup Bowl', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/6952058/pexels-photo-6952058.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product61 = Product(
        shop_id=1, name='Vase', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/6414823/pexels-photo-6414823.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product62 = Product(
        shop_id=1, name='Coffee Set', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/7674538/pexels-photo-7674538.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product63 = Product(
        shop_id=1, name='Dinner Plates', description='hand crafted', category='ceramics', price=29.99, image="https://images.pexels.com/photos/6694692/pexels-photo-6694692.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product64 = Product(
        shop_id=2, name='Deep Shiny and Mysterious', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/2113994/pexels-photo-2113994.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product65 = Product(
        shop_id=2, name='Lightweight Simple Stylish', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product66 = Product(
        shop_id=2, name='Basics Plain Sliver', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/280250/pexels-photo-280250.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product67 = Product(
        shop_id=2, name='Blue Backdrop Sliver Band', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/3766111/pexels-photo-3766111.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product68 = Product(
        shop_id=2, name='Basics, Essential', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/2783873/pexels-photo-2783873.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product69 = Product(
        shop_id=2, name='Simple but Elegant', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/3419331/pexels-photo-3419331.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product70 = Product(
        shop_id=2, name='Lightweight with Style', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/125779/pexels-photo-125779.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product71 = Product(
        shop_id=2, name='Refined sweet sliver blue backdrop', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/2799535/pexels-photo-2799535.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
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
