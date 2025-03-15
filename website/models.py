from . import db
from flask_login import UserMixin
from datetime import datetime, timezone

class User(db.Model, UserMixin):
    __tablename__ = "nomnom_user"  # Neuer Tabellenname

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    preparation = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('nomnom_user.id'))  # Neuer Tabellenname im ForeignKey

    user = db.relationship('User', backref='recipes')
