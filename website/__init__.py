from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import logging

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .views import views
    from .auth import auth  # 🔹 Auth-Blueprint registrieren
    app.register_blueprint(views)
    app.register_blueprint(auth)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"  # Verhindert ungewolltes Ausloggen
    login_manager.init_app(app)

    from .models import User, Recipe
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # 🔹 Logging aktivieren (hilft bei Debugging)
    logging.basicConfig(level=logging.INFO)
    
    # Rezepte automatisch hinzufügen
    with app.app_context():
        from .add_recipes import add_sample_recipes
        add_sample_recipes()

    return app
