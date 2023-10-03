from app.models import db, environment, SCHEMA, Image, Product
from sqlalchemy.sql import text

def seed_images():
    image0 = Image(
        product_id = 1, image1="https://images.pexels.com/photos/1705287/pexels-photo-1705287.jpeg")
    image1 = Image(
        product_id = 2, image1="https://images.pexels.com/photos/1705287/pexels-photo-1705287.jpeg")
    image2 = Image(
        product_id = 3, image1="https://images.pexels.com/photos/1705287/pexels-photo-1705287.jpeg")
    image3 = Image(
        product_id = 4, image1="https://images.pexels.com/photos/1705287/pexels-photo-1705287.jpeg")

    db.session.add(image0)
    db.session.add(image1)
    db.session.add(image2)
    db.session.add(image3)
    db.session.commit()


def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))

    db.session.commit()
