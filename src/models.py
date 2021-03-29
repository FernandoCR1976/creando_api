from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.db.Column(db.db.Integer, primary_key=True)
#     email = db.db.Column(db.db.String(120), unique=True, nullable=False)
#     password = db.db.Column(db.db.String(80), unique=False, nullable=False)
#     is_active = db.db.Column(db.Boolean(), unique=False, nullable=False)

   

class User_Fav(db.Model):
    __tablename__ = 'user_Fav'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    user_Fav = db.relationship(User_Fav)    

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(50))
    rotation_period = db.Column(db.Integer)
    orbital_period= db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(50))
    gravity= db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    population = db.Column(db.Integer)

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    heigth = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(50))

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_name = db.Column(db.String(50))
    model = db.Column(db.String(50))
    passengers = db.Column(db.Integer)
    consumable = db.Column(db.String(50))
    starship_class = db.Column(db.String(50))
    length = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    hyperdrive_rating = db.Column(db.Integer)



    def to_dict(self):
        return {}

