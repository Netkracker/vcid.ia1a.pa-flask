from website import create_app, db
from flask_migrate import Migrate

# Erstelle die Flask-App-Instanz mithilfe der Factory-Funktion
app = create_app()
# Initialisiere Flask-Migrate für die Verwaltung von Datenbankmigrationen
migrate = Migrate(app, db)
# Starte die Flask-Anwendung, wenn das Skript direkt ausgeführt wird
if __name__ == '__main__':
    app.run(debug=True)  # Debug-Modus aktivieren (nicht für Produktion empfohlen)