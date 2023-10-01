from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        profile_icon='https://images.pexels.com/photos/1460836/pexels-photo-1460836.jpeg', first_name = 'Demo' , last_name = 'Lition' , about = 'I love anything vintage' , birthday = '01/01/01' , address = '555 Disney Lane' , city = 'Dearborn' , state = 'Texas' , country = 'United States' , username='Demo', email='demo@aa.io', password='password')
    maria = User(
        profile_icon='https://images.pexels.com/photos/1460836/pexels-photo-1460836.jpeg', first_name ='Maria', last_name = 'Matter' , about = 'anything soft and fluffy I want it' , birthday = '02/02/02' , address = '123 House Mane' , city = 'Allen Park' , state = 'California' , country = 'United States' , username='maria', email='maria@aa.io', password='password')
    alex = User(
        profile_icon='https://images.pexels.com/photos/1460836/pexels-photo-1460836.jpeg', first_name = 'Alex' , last_name = 'Laruso' , about = 'Martial Arts' , birthday = '12/12/12' , address = '123 Home Town' , city = 'San Jose' , state = 'California' , country = 'United States' , username='alex', email='alex@aa.io', password='password')

    db.session.add(demo)
    db.session.add(maria)
    db.session.add(alex)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
