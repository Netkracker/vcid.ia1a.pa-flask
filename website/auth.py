from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

# 🔹 Benutzer registrieren
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("E-Mail bereits registriert!", "danger")
            return redirect(url_for('auth.register'))

        if password1 != password2:
            flash("Passwörter stimmen nicht überein!", "danger")
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Direkt nach Registrierung einloggen und zum Profil weiterleiten
        login_user(new_user)
        flash("Registrierung erfolgreich! Willkommen, {}!".format(name), "success")
        return redirect(url_for('views.profile'))  # 👈 Weiterleitung zur Profilseite

    return render_template("register.html")

# 🔹 Benutzer einloggen
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        # Einheitliche Fehlermeldung, um nicht preiszugeben, ob E-Mail oder Passwort falsch ist
        if not user or not check_password_hash(user.password, password):
            flash("E-Mail oder Passwort ist falsch!", "danger")
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('views.profile'))

    return render_template("login.html")

# 🔹 Benutzer ausloggen
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
