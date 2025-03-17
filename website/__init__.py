from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import logging

# Initialisierung der Datenbank
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    #Erstellt und konfiguriert die Flask-App.
    
    app = Flask(__name__)
    app.config.from_object(Config)  # Lädt die Konfiguration aus der Config-Klasse
    db.init_app(app)  # Initialisiert SQLAlchemy mit der App
    migrate.init_app(app, db)
    
    # logging to stdout for heroku
    if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)

    # Importieren und Registrieren der Blueprints für Views und Authentifizierung
    from .views import views
    from .auth import auth  
    app.register_blueprint(views)
    app.register_blueprint(auth)

    # Flask-Login Manager einrichten
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"  # Falls nicht eingeloggt, Weiterleitung zur Login-Seite
    login_manager.session_protection = "strong"  # Schutz vor Session-Hijacking
    login_manager.init_app(app)

    # Nutzer-Loader für Flask-Login
    from .models import User, Recipe
    @login_manager.user_loader
    def load_user(user_id):
        #Lädt einen Benutzer anhand der Benutzer-ID aus der Datenbank.
        return User.query.get(int(user_id))

    # Logging einrichten, um Fehler und Ereignisse besser nachverfolgen zu können
    logging.basicConfig(level=logging.INFO)

    # Automatisches Hinzufügen von Beispielrezepten beim Start der App
    with app.app_context():
        from .add_recipes import add_sample_recipes
        add_sample_recipes()

    return app
