from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email
            # do not serialize the password, it's a security breach
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(255), nullable = False)
    eye_color = db.Column(db.String(255), nullable = False)
    gender = db.Column(db.String(255), nullable = False)
    
    def __repr__(self):
        return '<Character %r>' % self.id
    
    def serialize(self):
        return {
        "id" : self.id,
        "name" : self.name,
        "eye_color" : self.eye_color,
        "gender" : self.gender
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    climate = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return '<Planet %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate
        }

class Starship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    passengers = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Starship %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "passengers": self.passengers
        }

class Favorite(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    starship_id = db.Column(db.Integer, db.ForeignKey('starship.id'), nullable=True)

    user = db.relationship('User', backref='favorites')
    planet = db.relationship('Planet', backref='favorites')
    character = db.relationship('Character', backref='favorites')
    starship = db.relationship('Starship', backref='favorites')

    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
            "starship_id": self.starship_id
        }