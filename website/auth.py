from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

# Blueprint für die Authentifizierungsrouten
auth = Blueprint('auth', __name__)

# Benutzer registrieren
@auth.route('/register', methods=['GET', 'POST'])
def register():
    #Ermöglicht Benutzern die Registrierung. Falls erfolgreich, werden sie automatisch eingeloggt.
    if request.method == 'POST':
        name = request.form.get('name')  # Benutzername aus dem Formular
        email = request.form.get('email')  # E-Mail-Adresse
        password1 = request.form.get('password1')  # Erstes Passwortfeld
        password2 = request.form.get('password2')  # Zweites Passwortfeld zur Bestätigung

        # Überprüfung, ob die E-Mail bereits registriert ist
        user = User.query.filter_by(email=email).first()
        if user:
            flash("E-Mail bereits registriert!", "danger")
            return redirect(url_for('auth.register'))

        # Überprüfung, ob die Passwörter übereinstimmen
        if password1 != password2:
            flash("Passwörter stimmen nicht überein!", "danger")
            return redirect(url_for('auth.register'))

        # Passwort sicher hashen und Benutzer speichern
        hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Direkt nach der Registrierung einloggen und zum Profil weiterleiten
        login_user(new_user)
        return redirect(url_for('views.profile'))  # Weiterleitung zur Profilseite

    return render_template("register.html")

# Benutzer einloggen
@auth.route('/login', methods=['GET', 'POST'])
def login():
    #Ermöglicht registrierten Benutzern das Einloggen.
    if request.method == 'POST':
        email = request.form.get('email')  # E-Mail-Adresse aus dem Formular
        password = request.form.get('password')  # Passwort aus dem Formular

        # Benutzer anhand der E-Mail-Adresse suchen
        user = User.query.filter_by(email=email).first()

        # Einheitliche Fehlermeldung, um nicht preiszugeben, ob E-Mail oder Passwort falsch ist
        if not user or not check_password_hash(user.password, password):
            flash("E-Mail oder Passwort ist falsch!", "danger")
            return redirect(url_for('auth.login'))

        # Benutzer einloggen und zur Profilseite weiterleiten
        login_user(user)
        return redirect(url_for('views.profile'))

    return render_template("login.html")

# Benutzer ausloggen
@auth.route('/logout')
@login_required
def logout():
    #Loggt den aktuellen Benutzer aus und leitet zur Startseite weiter.
    logout_user()
    return redirect(url_for('views.home'))
