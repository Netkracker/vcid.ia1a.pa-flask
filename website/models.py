from . import db
from flask_login import UserMixin
from datetime import datetime, timezone

# Benutzer-Modell für die Authentifizierung und Nutzerverwaltung
class User(db.Model, UserMixin):
    __tablename__ = "nomnom_user"  # Setzt den Tabellennamen explizit auf "nomnom_user"

    id = db.Column(db.Integer, primary_key=True)  # Eindeutige ID für jeden Benutzer
    name = db.Column(db.String(60), nullable=False)  # Name des Benutzers (Pflichtfeld)
    email = db.Column(db.String(100), unique=True, nullable=False)  # Eindeutige E-Mail-Adresse (Pflichtfeld)
    password = db.Column(db.String(150), nullable=False)  # Gespeichertes, gehashtes Passwort

# Rezept-Modell zur Speicherung von Rezepten
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Eindeutige ID für jedes Rezept
    title = db.Column(db.String(100), nullable=False)  # Titel des Rezepts (Pflichtfeld)
    ingredients = db.Column(db.Text, nullable=False)  # Zutatenliste (Pflichtfeld)
    preparation = db.Column(db.Text, nullable=False)  # Beschreibung der Zubereitung (Pflichtfeld)
    category = db.Column(db.String(20), nullable=False)  # Kategorie des Rezepts (z.B. "Vegetarisch", "Fleisch", etc.)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # Automatische Speicherung des Erstellungsdatums
    # Beziehung zum User-Modell: Jedes Rezept gehört einem Benutzer
    user_id = db.Column(db.Integer, db.ForeignKey('nomnom_user.id'))  # Referenz auf die User-Tabelle
    user = db.relationship('User', backref='recipes')  # Ermöglicht Zugriff auf die zugehörigen Rezepte eines Nutzers
