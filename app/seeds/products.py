

from app.models import db, Product, User, SCHEMA, environment
from sqlalchemy.sql import text

def seed_products():

    product0 = Product(
        shop_id=3, name='Ladyfingers', description='Finger-shaped pastries boast a delicate, flaky exterior that cradles a luxurious filling of coarsely ground nuts, commonly pistachios or walnuts. The nut mixture, enhanced with sugar and often a hint of cinnamon, delivers a sweet and nutty flavor profile that is both satisfying and indulgent. The pastry layers are meticulously crafted, providing a crisp texture that contrasts beautifully with the nutty interior. Typically they are either generously soaked in a fragrant sugar syrup, infusing them with a subtle sweetness, or adorned with a dusting of powdered sugar for an elegant finish. ', category='sweets', price=29.99, image="https://images.pexels.com/photos/7803117/pexels-photo-7803117.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product1= Product(
        shop_id=3, name='Baklava', description='Baklava, a jewel in the crown of Middle Eastern and Mediterranean sweets, is a divine pastry that captivates with its layers of delicate phyllo dough, finely chopped nuts, and a luscious honey or syrup infusion. This iconic dessert, with roots tracing back to the Ottoman Empire, is a masterpiece of craftsmanship and flavor. The layers of phyllo dough, paper-thin and expertly buttered, create a crisp and golden shell that encases a sumptuous blend of nuts—often a mix of walnuts, pistachios, and almonds—interspersed with aromatic spices such as cinnamon or cloves. Once baked to perfection, the baklava is generously drenched in a sweet syrup, often made with honey, sugar, and a hint of citrus, allowing each layer to soak up the sweetness and achieve a perfect balance of textures. The result is a dessert that is not only visually stunning with its diamond-shaped cuts but also an exquisite symphony of crispy, flaky, and syrupy goodness, making each bite a delightful journey into the heart of Middle Eastern culinary tradition.', category='sweets', price=50.12, image="https://images.pexels.com/photos/5323489/pexels-photo-5323489.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product2=Product(
        shop_id=3, name='Baklava', description='Baklava, a jewel in the crown of Middle Eastern and Mediterranean sweets, is a divine pastry that captivates with its layers of delicate phyllo dough, finely chopped nuts, and a luscious honey or syrup infusion. This iconic dessert, with roots tracing back to the Ottoman Empire, is a masterpiece of craftsmanship and flavor. The layers of phyllo dough, paper-thin and expertly buttered, create a crisp and golden shell that encases a sumptuous blend of nuts—often a mix of walnuts, pistachios, and almonds—interspersed with aromatic spices such as cinnamon or cloves. Once baked to perfection, the baklava is generously drenched in a sweet syrup, often made with honey, sugar, and a hint of citrus, allowing each layer to soak up the sweetness and achieve a perfect balance of textures. The result is a dessert that is not only visually stunning with its diamond-shaped cuts but also an exquisite symphony of crispy, flaky, and syrupy goodness, making each bite a delightful journey into the heart of Middle Eastern culinary tradition.', category='sweets', price=5, image="https://images.pexels.com/photos/17255931/pexels-photo-17255931/free-photo-of-close-up-of-slices-of-baklava.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300",image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product3 = Product(
        shop_id=3, name='Turkish Delight', description='Turkish Delight, or "lokum," is a confectionary treasure that has enchanted palates for centuries with its unique chewy texture and enticing blend of flavors. This sweet delight, originating from the Ottoman Empire, is crafted from sugar, starch, water, and a variety of flavorings. The mixture is meticulously cooked and then poured into molds to set into soft, bite-sized cubes. Rosewater, orange blossom, or lemon are common traditional flavorings, each imparting a fragrant and exotic note to the candy. Often, these delectable morsels are coated in a dusting of powdered sugar or desiccated coconut to prevent sticking. The result is a confection that delights the senses, offering a satisfying chewiness and a burst of floral or fruity sweetness. Turkish Delight holds a special place in cultural traditions and is frequently enjoyed with a cup of tea, embodying the essence of hospitality and indulgence in Middle Eastern and Turkish culinary heritage.', category='sweets', price=29.99, image="https://images.pexels.com/photos/6161509/pexels-photo-6161509.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300",image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product4 = Product(
        shop_id=3, name='Baklava', description='Baklava, a jewel in the crown of Middle Eastern and Mediterranean sweets, is a divine pastry that captivates with its layers of delicate phyllo dough, finely chopped nuts, and a luscious honey or syrup infusion. This iconic dessert, with roots tracing back to the Ottoman Empire, is a masterpiece of craftsmanship and flavor. The layers of phyllo dough, paper-thin and expertly buttered, create a crisp and golden shell that encases a sumptuous blend of nuts—often a mix of walnuts, pistachios, and almonds—interspersed with aromatic spices such as cinnamon or cloves. Once baked to perfection, the baklava is generously drenched in a sweet syrup, often made with honey, sugar, and a hint of citrus, allowing each layer to soak up the sweetness and achieve a perfect balance of textures. The result is a dessert that is not only visually stunning with its diamond-shaped cuts but also an exquisite symphony of crispy, flaky, and syrupy goodness, making each bite a delightful journey into the heart of Middle Eastern culinary tradition.', category='sweets', price=29.99, image="https://images.pexels.com/photos/17255923/pexels-photo-17255923/free-photo-of-close-up-of-kadayif-baklava.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product5 = Product(
        shop_id=3, name='Kunafa', description='Kunafa, a splendid and indulgent dessert hailing from the Middle East, is a masterpiece of crispy and creamy textures harmonized with a symphony of flavors. This delectable treat is crafted by layering shredded phyllo dough or semolina noodles, creating a base that alternates between crisp and tender. The layers embrace a rich filling, often a blend of sweetened cheese such as akkawi or mozzarella, though variations can include cream or nuts, adding a luxurious depth to the dessert. Once baked to golden perfection, kunafa is drenched in a fragrant sugar-based syrup, often infused with rose or orange blossom water, enhancing its sweetness and infusing it with an irresistible aroma. The juxtaposition of the crunchy exterior and the creamy, luscious interior makes every bite a sensory delight, epitomizing the artistry of Middle Eastern sweets and the richness of its culinary heritage. Whether enjoyed warm or at room temperature, kunafa remains an iconic and beloved delicacy, symbolizing the essence of hospitality and celebration in the region.', category='sweets', price=29.99, image="https://images.pexels.com/photos/11833316/pexels-photo-11833316.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product6 = Product(
        shop_id=3, name='Pudding', description="Pudding, a classic and comforting dessert enjoyed worldwide, is a testament to the simple yet delightful pleasures of sweet indulgence. Crafted in various forms across cultures, pudding is fundamentally a creamy and smooth concoction made from milk, sugar, and a thickening agent like cornstarch or eggs. The beauty of pudding lies in its versatility, allowing for a myriad of flavor profiles. Whether it's the velvety richness of chocolate, the fragrant warmth of vanilla, or the subtle sophistication of butterscotch, pudding captivates taste buds with its luscious texture and sweet essence. Often served chilled or at room temperature, pudding is a canvas for creative toppings such as whipped cream, fruit compotes, or a sprinkle of nuts. Its universal appeal lies in the comforting simplicity of a dessert that evokes a sense of nostalgia and satisfies the craving for a sweet, creamy treat. Whether enjoyed on its own or as part of a more elaborate dessert, pudding remains a timeless delight that transcends culinary boundaries.", category='sweets', price=29.99, image="https://images.pexels.com/photos/3547176/pexels-photo-3547176.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product7 = Product(
        shop_id=3, name='Macaron', description="Macarons, not to be confused with the coconut-based macaroons, are delicate and dainty French pastries that epitomize the artistry of patisserie. These small, round confections consist of two almond meringue shells that delicately sandwich a flavorful ganache, buttercream, or jam filling. The macaron's hallmark is its smooth, shiny exterior, achieved through a meticulous process of folding almond flour and powdered sugar into egg whites. The result is a thin, crisp shell that encapsulates a chewy interior, creating a delightful textural contrast. Macarons come in a rainbow of colors and an array of flavors, from classic options like vanilla and chocolate to more exotic choices such as lavender or pistachio. With their elegant appearance and diverse taste offerings, macarons have become a symbol of sophistication in the world of desserts, making them a sought-after treat for both special occasions and everyday indulgence.", category='sweets', price=29.99, image="https://images.pexels.com/photos/7474290/pexels-photo-7474290.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product8 = Product(
        shop_id=3, name='Berry Blast', description='Berry Blast Dessert is a vibrant and refreshing culinary creation that celebrates the natural sweetness and tartness of various berries. This delightful dessert is a medley of luscious berries such as strawberries, blueberries, raspberries, and blackberries, each contributing its unique flavor profile and vibrant color. The berries are often layered atop a base of velvety whipped cream, yogurt, or a light sponge cake, creating a harmonious blend of textures. A drizzle of berry coulis or a sprinkle of powdered sugar adds a touch of elegance, enhancing the visual appeal and flavor complexity. The result is a burst of fruity freshness with every spoonful, offering a delightful balance of sweetness and acidity. Whether served in individual portions or as a stunning centerpiece for a larger gathering, the Berry Blast Dessert is a celebration of seasonal bounty and a joyful exploration of the bountiful flavors nature has to offer.', category='sweets', price=29.99, image="https://images.pexels.com/photos/2693447/pexels-photo-2693447.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300", image5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product9 = Product(
        shop_id=3, name='Choclate Eclair', description='Chocolate Eclair, a timeless and indulgent pastry, is a masterpiece that marries simplicity with decadence. This classic French dessert consists of a delicate elongated pastry shell, crafted from choux dough, that is baked until golden and hollow inside. The shell is then filled with a velvety, vanilla custard or pastry cream, imparting a rich and creamy interior. The crowning glory comes in the form of a glossy chocolate ganache, which enrobes the eclair in a layer of bittersweet decadence. The textural interplay between the crisp choux pastry, the smooth and cool custard, and the luxuriously glossy chocolate coating creates a symphony of flavors and sensations. The Chocolate Eclair stands as a testament to the art of French patisserie, offering a perfect balance of sweetness and sophistication in each delightful bite. Whether enjoyed as a standalone treat or as the pièce de résistance in an elegant dessert spread, the Chocolate Eclair remains an enduring symbol of culinary refinement.', category='sweets', price=29.99, image="https://images.pexels.com/photos/5945568/pexels-photo-5945568.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product10 = Product(
        shop_id=3, name='Assortment Variety', description='hand crafted', category='sweets', price=29.99, image="https://images.pexels.com/photos/4913389/pexels-photo-4913389.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product11 = Product(
        shop_id=3, name='Pistachio layered Ice Cream', description='Pistachio Layered Ice Cream is a sublime frozen indulgence that combines the earthy richness of pistachios with the creamy allure of ice cream. This dessert masterpiece features layers of velvety pistachio-flavored ice cream, each stratum offering a symphony of nutty undertones and a vibrant green hue. The base ice cream, often made with a combination of finely ground pistachios, milk, cream, and sugar, achieves a luxurious texture that is both smooth and satisfying. Intertwined with the pistachio layers are ribbons of decadent chocolate fudge or swirls of pistachio sauce, adding an extra layer of complexity to the flavor profile. The result is a harmonious fusion of sweet and nutty, with occasional bursts of chocolatey indulgence. Whether served in a cone, bowl, or as part of an elaborate ice cream sundae, the Pistachio Layered Ice Cream stands as a testament to the art of frozen desserts, providing a refreshing and indulgent treat that captivates the senses with every spoonful.', category='sweets', price=29.99, image="https://images.pexels.com/photos/13020802/pexels-photo-13020802.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product12 = Product(
        shop_id=3, name='Nuts Cream and Choclate', description='A divine fusion of textures and flavors, offering a symphony of nuttiness and chocolatey decadence. This delectable creation typically features layers of silky chocolate mousse or ganache alternated with velvety whipped cream that has been delicately infused with a medley of finely chopped nuts—such as almonds, hazelnuts, and walnuts. The nuts contribute a delightful crunch and a rich, earthy undertone, enhancing the overall sensory experience. The dessert is often adorned with a drizzle of glossy chocolate sauce, creating a visually appealing and indulgent masterpiece. With each spoonful, one encounters the luscious creaminess of the whipped cream, the satisfying crunch of the nuts, and the luxurious depth of the chocolate, resulting in a harmonious blend that caters to both the sweet tooth and the craving for nutty textures. ', category='sweets', price=29.99, image="https://images.pexels.com/photos/7783241/pexels-photo-7783241.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product13 = Product(
        shop_id=3, name='Pudding', description="Pudding, a classic and comforting dessert enjoyed worldwide, is a testament to the simple yet delightful pleasures of sweet indulgence. Crafted in various forms across cultures, pudding is fundamentally a creamy and smooth concoction made from milk, sugar, and a thickening agent like cornstarch or eggs. The beauty of pudding lies in its versatility, allowing for a myriad of flavor profiles. Whether it's the velvety richness of chocolate, the fragrant warmth of vanilla, or the subtle sophistication of butterscotch, pudding captivates taste buds with its luscious texture and sweet essence. Often served chilled or at room temperature, pudding is a canvas for creative toppings such as whipped cream, fruit compotes, or a sprinkle of nuts. Its universal appeal lies in the comforting simplicity of a dessert that evokes a sense of nostalgia and satisfies the craving for a sweet, creamy treat. Whether enjoyed on its own or as part of a more elaborate dessert, pudding remains a timeless delight that transcends culinary boundaries.", category='sweets', price=29.99, image="https://images.pexels.com/photos/3026810/pexels-photo-3026810.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
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
        shop_id=2, name='Golden Thin Bangles', description="Golden Bangles, as exquisite jewelry pieces, embody a timeless elegance and cultural significance. Crafted with precision and artistry, these accessories are often made from lustrous gold, showcasing intricate designs that range from traditional to contemporary. Their circular form symbolizes unity and eternity, making them popular choices for celebratory occasions such as weddings and festivals. The beauty of golden bangles lies not only in their craftsmanship but also in their versatility, seamlessly complementing both traditional and modern attire. These adornments add a touch of sophistication and opulence to any ensemble, reflecting the wearer's personal style and celebrating the cultural heritage from which they draw inspiration. Whether worn as a single statement piece or stacked in multiples for a bolder look, golden bangles are more than just accessories; they are tangible expressions of tradition, craftsmanship, and the enduring allure of gold in the realm of fine jewelry.", category='jewelry', price=29.99, image="https://images.pexels.com/photos/7992686/pexels-photo-7992686.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product31 = Product(
        shop_id=2, name='Rose Gold Diamond Earnings', description="Rose Gold Diamond Earrings embody the pinnacle of sophistication, seamlessly blending the romantic allure of rose gold with the timeless brilliance of diamonds. Crafted with meticulous attention to detail, these earrings showcase the delicate interplay between the warm, rosy tones of the gold setting and the dazzling sparkle of the diamonds. The rose gold serves as an exquisite backdrop, imparting a soft and feminine touch to the overall design. Diamonds, renowned for their exceptional clarity and brilliance, add a touch of opulence and refinement to the earrings. Whether arranged in classic stud settings, dangling from delicate hoops, or intricately incorporated into more elaborate designs, rose gold diamond earrings are a symbol of enduring love and luxury. These earrings effortlessly transition from everyday elegance to special occasions, making them a versatile and cherished addition to any jewelry collection. The combination of rose gold and diamonds creates a harmonious fusion of romantic allure and timeless sophistication, elevating these earrings to the realm of coveted and treasured accessories.", category='jewelry', price=29.99, image="https://images.pexels.com/photos/10983783/pexels-photo-10983783.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product32 = Product(
        shop_id=2, name='Embedded Diamonds', description="Jewelry with Embedded Diamonds radiates opulence and refinement, showcasing the perfect marriage of precious metals and the timeless allure of diamonds. These meticulously crafted pieces, whether rings, necklaces, bracelets, or earrings, feature diamonds strategically embedded into the design, creating a stunning interplay of light and luxury. The setting, often made of white gold, yellow gold, rose gold, or platinum, serves as a tasteful backdrop to accentuate the diamonds' brilliance. The arrangement and design can range from classic and understated to more intricate and contemporary, offering a diverse array of options to suit individual tastes. Whether in a solitaire setting or as part of a complex pattern, jewelry with embedded diamonds exudes sophistication, making it a coveted choice for special occasions and a timeless investment in the world of fine jewelry. These pieces become not just accessories but expressions of enduring elegance and an appreciation for the rare and precious beauty of diamonds.", category='jewelry', price=29.99, image="https://images.pexels.com/photos/265906/pexels-photo-265906.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product33 = Product(
        shop_id=2, name='Feathery Earings', description="Feathery Earrings evoke a sense of ethereal grace and lightness, capturing the delicate beauty of feathers in a wearable art form. Crafted with meticulous detail, these earrings feature intricately designed feathers that may be made of various materials, such as metal, fabric, or even real feathers, to create a lightweight and airy aesthetic. The feathery elements gently sway with movement, adding a touch of fluidity and playfulness to the overall design. Whether fashioned as dainty drops, elaborate cascading styles, or simple stud earrings, feathery earrings bring a whimsical and bohemian flair to any ensemble. The fine balance between the delicate nature of feathers and the artful craftsmanship results in earrings that are not just accessories but expressions of free-spirited elegance. Whether worn casually or to make a statement on a special occasion, feathery earrings are a unique and stylish way to infuse a sense of lightness and natural beauty into one's jewelry collection.", category='jewelry', price=29.99, image="https://images.pexels.com/photos/1413420/pexels-photo-1413420.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product34 = Product(
        shop_id=2, name='Sterling Silver Ring', description="Sterling Silver Rings embody a timeless allure with their understated elegance and versatile appeal. Crafted from 92.5% pure silver, blended with a small percentage of alloy for added strength, these rings offer a lustrous and durable alternative to more traditional precious metals. The cool, sleek sheen of sterling silver complements a variety of styles, making these rings a staple in any jewelry collection. Whether adorned with minimalist engravings, set with gemstones, or left unadorned for a classic look, sterling silver rings effortlessly transition from casual to formal wear. The versatility of sterling silver makes it an ideal canvas for both contemporary and vintage-inspired designs. Beyond their aesthetic charm, these rings often hold sentimental value as symbols of commitment, friendship, or personal style. As enduring pieces that withstand the test of time, sterling silver rings celebrate simplicity, sophistication, and the enduring beauty of this precious metal.", category='jewelry', price=29.99, image="https://images.pexels.com/photos/3266703/pexels-photo-3266703.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product35 = Product(
        shop_id=2, name='Blue Topaz Sliver', description="A Blue Topaz Sterling Silver Ring combines the enchanting allure of a vibrant gemstone with the sleek elegance of sterling silver, creating a striking and versatile piece of jewelry. The focal point of the ring is the mesmerizing blue topaz, a gemstone known for its cool, azure hues that evoke the tranquility of the sea and the sky. Set against the backdrop of polished sterling silver, the blue topaz takes center stage, creating a harmonious and eye-catching contrast. The setting may vary, ranging from simple solitaire designs to more intricate arrangements that incorporate additional gemstones or intricate detailing. The sterling silver band adds a touch of sophistication and modernity, making the ring suitable for both everyday wear and special occasions. Whether worn as a statement piece or as a symbol of personal style, the Blue Topaz Sterling Silver Ring is a captivating accessory that blends the timeless elegance of sterling silver with the mesmerizing beauty of a gemstone, resulting in a piece that is both refined and eye-catching.", category='jewelry', price=29.99, image="https://images.pexels.com/photos/2697598/pexels-photo-2697598.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product36 = Product(
        shop_id=2, name='Cubed Sterling Silver necklace', description="A Cubed Sterling Silver Necklace brings a modern and geometric flair to the world of jewelry. Crafted with precision, this necklace features a pendant composed of sleek and polished sterling silver cubes, arranged in a chic and contemporary design. The cube's clean lines and crisp edges add a touch of architectural sophistication to the piece, creating a visual appeal that is both sleek and versatile. The pendant's geometric structure not only reflects a minimalist aesthetic but also plays with light to create an eye-catching and dynamic effect. Suspended from a sterling silver chain, the necklace balances a sense of simplicity with a bold and modern edge. Whether worn as a standalone accessory for a polished and modern look or layered with other pieces for a more eclectic style, the Cubed Sterling Silver Necklace effortlessly transitions from casual to formal occasions, making it a versatile and fashion-forward addition to any jewelry collection.", category='jewelry', price=29.99, image="https://images.pexels.com/photos/2697616/pexels-photo-2697616.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product37 = Product(
        shop_id=2, name='Diamond Embeded necklace', description="A Necklace Embedded with Diamonds exudes opulence and timeless sophistication. Crafted with meticulous precision, this necklace features a stunning arrangement of diamonds strategically embedded into the design, creating a captivating interplay of light and luxury. The diamonds, renowned for their brilliance and clarity, form a mesmerizing focal point, adding a touch of glamour and elegance to the piece. The setting, often crafted from precious metals like white gold or platinum, serves as a refined backdrop to enhance the diamonds' brilliance. The necklace may showcase a variety of designs, from classic and understated to more intricate and contemporary arrangements, each highlighting the radiant beauty of the embedded diamonds. Whether worn as a statement piece for a special occasion or as an everyday symbol of enduring luxury, the Necklace Embedded with Diamonds is a timeless accessory that elevates any ensemble with its dazzling sparkle and undeniable allure.", category='jewelry', price=29.99, image="https://images.pexels.com/photos/4595719/pexels-photo-4595719.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
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
        shop_id=2, name='Gold beaded bracelet', description="A Gold Heart Pendant Necklace embodies a timeless symbol of love and elegance, blending the warmth of gold with the sentimental charm of a heart-shaped pendant. Crafted with care and artistry, this necklace features a heart-shaped charm made from lustrous gold, serving as a radiant centerpiece. The smooth and polished surface of the gold adds a touch of sophistication to the piece. The heart, a universal symbol of affection and emotion, infuses the necklace with sentimental value, making it a cherished accessory for special occasions or as a heartfelt gift. The pendant may vary in design, from classic and understated to more intricate and embellished styles, allowing for personalization to suit individual tastes. Suspended from a delicate gold chain, the necklace beautifully frames the heart, creating a piece that is both timeless and meaningful. The Gold Heart Pendant Necklace is not merely jewelry; it is a wearable expression of love and enduring elegance, making it a classic and sentimental addition to any jewelry collection.", category='jewelry', price=29.99, image="https://images.pexels.com/photos/11260679/pexels-photo-11260679.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product42 = Product(
        shop_id=1, name='Spiral Drill Tip', description="A Spiral Drill Tip, an essential accessory for power drills, epitomizes precision and efficiency in various drilling applications. Crafted with high-quality materials and engineering, this drill tip features a helical spiral design that enhances drilling performance. The spiraled shape aids in efficient material removal, reducing friction and heat buildup during drilling. This design is particularly advantageous in creating clean and precise holes, making it suitable for a variety of materials, from wood and metal to plastic. The Spiral Drill Tip's grooved configuration helps to channel debris away from the drilling site, minimizing the risk of overheating and enhancing the overall durability of the tool. The helical structure also contributes to improved drilling accuracy and stability. Whether used by professionals or DIY enthusiasts, the Spiral Drill Tip stands out as a reliable and versatile accessory, embodying the principles of functionality, durability, and precision in the realm of drilling tools.", category='tools', price=29.99, image="https://images.pexels.com/photos/47091/drill-milling-milling-machine-drilling-47091.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product43 = Product(
        shop_id=1, name='Drilling Machine', description="A drilling machine is an indispensable tool in workshops and construction sites, epitomizing precision and power. Crafted with robust materials and advanced engineering, it boasts a sturdy design and a powerful motor, capable of driving various drill bits through materials like wood, metal, plastic, and masonry. The machine's adjustable speed settings, torque control, and quick-change chuck system enhance its versatility, allowing for tailored drilling experiences in diverse applications. Whether used by professionals or DIY enthusiasts, the drilling machine stands as a reliable and efficient tool, embodying durability, precision, and adaptability in the realm of drilling tools.", category='tools', price=29.99, image="https://images.pexels.com/photos/5974042/pexels-photo-5974042.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product44 = Product(
        shop_id=1, name='Compelete Wrench Set', description="A complete wrench set is the cornerstone of any well-equipped toolkit, embodying versatility, durability, and precision. Crafted with high-quality materials and meticulous engineering, the set typically includes a variety of wrench sizes and types, each designed to tackle specific tasks with ease. The wrenches, whether adjustable or fixed, showcase ergonomic designs for comfortable handling and efficient torque application. With their durable construction, the wrenches provide the strength needed for turning nuts and bolts in various applications, making them essential for both professional mechanics and DIY enthusiasts. The comprehensive nature of a complete wrench set ensures that it can handle a wide array of tasks, from automotive repairs to household maintenance, showcasing its indispensable role in facilitating efficient and reliable wrenching operations.", category='tools', price=29.99, image="https://images.pexels.com/photos/162553/keys-workshop-mechanic-tools-162553.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product45 = Product(
        shop_id=1, name='Wrench', description="A wrench, a fundamental tool in any toolkit, represents the embodiment of simplicity, utility, and mechanical efficiency. Crafted from sturdy materials such as steel, a wrench typically features a handle and a fixed or adjustable jaw designed to grip nuts and bolts securely. The ergonomic design of the handle ensures a comfortable grip for users, while the jaws provide the necessary leverage to tighten or loosen fasteners. Whether it's a classic crescent wrench, an adjustable wrench, or a specialized wrench for plumbing or automotive work, this timeless tool showcases adaptability for various applications. The straightforward yet ingenious design of a wrench highlights its role as an essential and versatile tool, symbolizing the essence of practicality and effectiveness in the world of hand tools.", category='tools', price=29.99, image="https://images.pexels.com/photos/5691629/pexels-photo-5691629.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product46 = Product(
        shop_id=1, name='Nuts and Bolts', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/8780720/pexels-photo-8780720.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product47 = Product(
        shop_id=1, name='Drill Tip', description='hand crafted', category='tools', price=29.99, image="https://images.pexels.com/photos/50691/drill-milling-milling-machine-drilling-50691.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product48 = Product(
        shop_id=1, name='Gears', description="Gears, intricate mechanical components, epitomize the essence of precision engineering and functional elegance. Crafted with meticulous attention to detail, gears consist of toothed wheels designed to interlock seamlessly, transferring motion and power with remarkable efficiency. Whether found in machinery, vehicles, or intricate clockwork mechanisms, gears play a pivotal role in translating rotational force into controlled movement. The design of gears reflects a delicate balance between tooth size, pitch, and alignment, ensuring smooth engagement and minimizing friction. This mechanical ingenuity allows gears to transmit power reliably while maintaining a consistent speed ratio. Gears symbolize the symbiosis of form and function, embodying the essence of mechanical precision and the crucial role they play in the seamless operation of countless devices and systems.", category='tools', price=29.99, image="https://images.pexels.com/photos/3785929/pexels-photo-3785929.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
    )
    product49 = Product(
        shop_id=1, name='Gear Set', description="A gear set is a harmonious ensemble of precision-engineered components that collectively embody the seamless integration of form and function. Comprising interlocking toothed wheels of varying sizes and configurations, a gear set operates in unison to transmit motion and power with exceptional efficiency. Crafted with meticulous precision, each gear within the set is designed to mesh seamlessly with its counterparts, ensuring a synchronized transfer of rotational force. The arrangement and ratio of gears within the set are paramount, determining the speed, torque, and direction of the system they power. From intricate clock mechanisms to complex industrial machinery, a gear set's ability to translate input into controlled and reliable output defines its significance in the realm of mechanical engineering. The cohesion of these precisely crafted gears represents a testament to the art and science of gear design, showcasing their indispensable role in the functionality and efficiency of countless mechanical systems.", category='tools', price=29.99, image="https://images.pexels.com/photos/414579/pexels-photo-414579.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
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
        shop_id=2, name='Sliver Blue Backdrop', description='hand crafted', category='watches', price=29.99, image="https://images.pexels.com/photos/2799535/pexels-photo-2799535.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=300&w=300"
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
