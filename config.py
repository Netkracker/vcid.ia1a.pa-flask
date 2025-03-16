import os

class Config:
    # Geheimer Schlüssel für die Flask-Session und Sicherheitsfunktionen (z. B. CSRF-Schutz)
    SECRET_KEY = os.getenv("SECRET_KEY", "supergeheimespasswort")
    # Datenbankverbindung: Nutzt eine Umgebungsvariable oder eine lokale PostgreSQL-Datenbank als Fallback
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://postgres:Welcome$2025@localhost/nomnom")
    # Deaktiviert das Tracking von Modifikationen durch SQLAlchemy, um Ressourcen zu sparen
    SQLALCHEMY_TRACK_MODIFICATIONS = False