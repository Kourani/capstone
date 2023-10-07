from app.models import db, environment, SCHEMA, Image, Product
from sqlalchemy.sql import text

def seed_images():
    image0 = Image(
        product_id = 1, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image1 = Image(
         product_id = 2, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image2 = Image(
         product_id = 3, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image3 = Image(
         product_id = 4, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image4 = Image(
        product_id = 5, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image5 = Image(
         product_id = 6, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image6 = Image(
         product_id = 7, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image7 = Image(
         product_id = 8, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image8 = Image(
        product_id = 9, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image9 = Image(
         product_id = 10, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image10 = Image(
         product_id = 11, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image11 = Image(
         product_id = 12, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image12 = Image(
        product_id = 13, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image13 = Image(
         product_id = 14, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image14 = Image(
         product_id = 15, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image15 = Image(
         product_id = 16, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image16 = Image(
        product_id = 17, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image17 = Image(
         product_id = 18, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image18 = Image(
         product_id = 19, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image19 = Image(
         product_id = 20, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image20 = Image(
        product_id = 21, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image21 = Image(
         product_id = 22, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image22 = Image(
         product_id = 23, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image23 = Image(
         product_id = 24, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image24 = Image(
        product_id = 25, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image25 = Image(
         product_id = 26, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image26 = Image(
         product_id = 27, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image27 = Image(
         product_id = 28, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image28 = Image(
        product_id = 29, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image29 = Image(
         product_id = 30, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image30 = Image(
         product_id = 31, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image31 = Image(
         product_id = 32, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image32 = Image(
        product_id = 33, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image33 = Image(
         product_id = 34, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image34 = Image(
         product_id = 35, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image35 = Image(
         product_id = 36, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image36 = Image(
        product_id = 37, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image37 = Image(
         product_id = 38, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image38 = Image(
         product_id = 39, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image39 = Image(
         product_id = 40, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image40 = Image(
        product_id = 41, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image41 = Image(
         product_id = 42, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image42 = Image(
         product_id = 43, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image43 = Image(
         product_id = 44, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image44 = Image(
        product_id = 45, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image45 = Image(
         product_id = 46, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image46 = Image(
         product_id = 47, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image47 = Image(
         product_id = 48, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image48 = Image(
        product_id = 49, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image49 = Image(
         product_id = 50, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image50 = Image(
         product_id = 51, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image51 = Image(
         product_id = 52, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image52 = Image(
        product_id = 53, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image53 = Image(
         product_id = 54, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image54 = Image(
         product_id = 55, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image55 = Image(
         product_id = 56, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image56 = Image(
        product_id = 57, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image57 = Image(
         product_id = 58, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image58 = Image(
         product_id = 59, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image59 = Image(
         product_id = 60, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image60 = Image(
        product_id = 61, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image61 = Image(
         product_id = 62, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image62 = Image(
         product_id = 63, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image63 = Image(
         product_id = 64, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image64 = Image(
        product_id = 65, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image65 = Image(
         product_id = 66, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image66 = Image(
         product_id = 67, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image67 = Image(
         product_id = 68, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image68 = Image(
        product_id = 69, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image69 = Image(
         product_id = 70, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image70 = Image(
         product_id = 71, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")
    image71 = Image(
         product_id = 72, image_1="https://images.pexels.com/photos/1496373/pexels-photo-1496373.jpeg", image_2="https://images.pexels.com/photos/2591408/pexels-photo-2591408.jpeg", image_3="https://images.pexels.com/photos/1496378/pexels-photo-1496378.jpeg", image_4="https://images.pexels.com/photos/1083515/pexels-photo-1083515.jpeg", image_5="https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg")

    db.session.add(image0)
    db.session.add(image1)
    db.session.add(image2)
    db.session.add(image3)
    db.session.add(image4)
    db.session.add(image5)
    db.session.add(image6)
    db.session.add(image7)
    db.session.add(image8)
    db.session.add(image9)
    db.session.add(image10)
    db.session.add(image11)
    db.session.add(image12)
    db.session.add(image13)
    db.session.add(image14)
    db.session.add(image15)
    db.session.add(image16)
    db.session.add(image17)
    db.session.add(image18)
    db.session.add(image19)
    db.session.add(image20)
    db.session.add(image21)
    db.session.add(image22)
    db.session.add(image23)
    db.session.add(image24)
    db.session.add(image25)
    db.session.add(image26)
    db.session.add(image27)
    db.session.add(image28)
    db.session.add(image29)
    db.session.add(image30)
    db.session.add(image31)
    db.session.add(image32)
    db.session.add(image33)
    db.session.add(image34)
    db.session.add(image35)
    db.session.add(image36)
    db.session.add(image37)
    db.session.add(image38)
    db.session.add(image39)
    db.session.add(image40)
    db.session.add(image41)
    db.session.add(image42)
    db.session.add(image43)
    db.session.add(image44)
    db.session.add(image45)
    db.session.add(image46)
    db.session.add(image47)
    db.session.add(image48)
    db.session.add(image49)
    db.session.add(image50)
    db.session.add(image51)
    db.session.add(image52)
    db.session.add(image53)
    db.session.add(image54)
    db.session.add(image55)
    db.session.add(image56)
    db.session.add(image57)
    db.session.add(image58)
    db.session.add(image59)
    db.session.add(image60)
    db.session.add(image61)
    db.session.add(image62)
    db.session.add(image63)
    db.session.add(image64)
    db.session.add(image65)
    db.session.add(image66)
    db.session.add(image67)
    db.session.add(image68)
    db.session.add(image69)
    db.session.add(image70)
    db.session.add(image71)

    db.session.commit()


def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))

    db.session.commit()
