# views.py - Flask-Routen für NomNom
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from .models import db, Recipe  # Importiere das Recipe-Modell
 
# Initialisiere Blueprint für die Views
views = Blueprint('views', __name__)

# Startseite mit den neuesten Rezepten
@views.route('/')
def home():
    recipes = Recipe.query.order_by(Recipe.created_at.desc()).limit(6).all()
    print(f"Gefundene Rezepte: {recipes}")  # Debugging in Konsole
    return render_template("home.html", recipes=recipes)

# Rezeptsuche mit optionalem Suchbegriff
@views.route('/recipe_search', methods=['GET'])
def recipe_search():
    query = request.args.get('q', '')  # Suchbegriff aus der URL holen
    if query:
        recipes = Recipe.query.filter(Recipe.title.ilike(f"%{query}%")).all()
    else:
        recipes = Recipe.query.all()  # Falls kein Suchbegriff, alle Rezepte anzeigen
    return render_template("recipe_search.html", recipes=recipes, query=query)

# Einzelnes Rezept anzeigen (Kein Login erforderlich)
@views.route('/recipe_details/<int:recipe_id>')
def recipe_details(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)  # Holt das Rezept oder gibt 404 zurück
    return render_template("recipe_details.html", recipe=recipe)

# Neues Rezept erstellen (Login erforderlich)
@views.route('/recipe_create', methods=['GET', 'POST'])
@login_required  # Nur eingeloggte Nutzer dürfen Rezepte erstellen
def recipe_create():
    if request.method == 'POST':
        title = request.form.get('title')
        ingredients = request.form.get('ingredients')
        preparation = request.form.get('preparation')
        category = request.form.get('category')

        # Validierung: Sind alle Felder ausgefüllt?
        if not title or not ingredients or not preparation or not category:
            flash("Bitte fülle alle Felder aus!", "danger")
            return redirect(url_for('views.recipe_create'))

        # Neues Rezept anlegen
        new_recipe = Recipe(
            title=title,
            ingredients=ingredients,
            preparation=preparation,
            category=category,
            user_id=current_user.id  # Das Rezept gehört dem eingeloggten Nutzer
        )

        try:
            db.session.add(new_recipe)
            db.session.commit()
            return redirect(url_for('views.home'))  # Weiterleitung zur Startseite
        except Exception as e:
            db.session.rollback()
            flash("Fehler beim Speichern des Rezepts!", "danger")
            print(f"Fehler: {e}")  # Debugging-Ausgabe in der Konsole

    return render_template("recipe_create.html")

# Rezept bearbeiten (Login erforderlich)
@views.route('/recipe_edit/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def recipe_edit(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    # Prüfen, ob der aktuelle Benutzer der Besitzer des Rezepts ist
    if recipe.user_id != current_user.id:
        flash("Du kannst nur deine eigenen Rezepte bearbeiten!", "danger")
        return redirect(url_for('views.recipe_details', recipe_id=recipe_id))

    if request.method == 'POST':
        recipe.title = request.form.get('title')
        recipe.ingredients = request.form.get('ingredients')
        recipe.preparation = request.form.get('preparation')
        recipe.category = request.form.get('category')

        db.session.commit()
        return redirect(url_for('views.recipe_details', recipe_id=recipe_id))

    return render_template("recipe_edit.html", recipe=recipe)

# Rezept löschen (Login erforderlich)
@views.route('/recipe_delete/<int:recipe_id>', methods=['POST'])
@login_required
def recipe_delete(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    # Prüfen, ob der aktuelle Benutzer der Besitzer des Rezepts ist
    if recipe.user_id != current_user.id:
        flash("Du kannst nur deine eigenen Rezepte löschen!", "danger")
        return redirect(url_for('views.recipe_details', recipe_id=recipe_id))

    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('views.profile'))  # Zur Profilseite, wo alle eigenen Rezepte sind

# Über-Seite (Kein Login erforderlich)
@views.route('/about')
def about():
    return render_template("about.html")

# Login-Seite
@views.route('/login')
def login():
    return render_template("login.html")

# Registrierungs-Seite
@views.route('/register')
def register():
    return render_template("register.html")

# Profilseite: Zeigt alle Rezepte des eingeloggten Benutzers
@views.route('/profile')
@login_required
def profile():
    recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    return render_template("profile.html", recipes=recipes)

# API-Endpunkt für das Abrufen aller Rezepte (öffentlicher Zugriff)
@views.route('/api/recipes', methods=['GET'])
def api_get_recipes():
    recipes = Recipe.query.order_by(Recipe.created_at.desc()).all()

    # Rezepte in JSON umwandeln
    recipes_json = [
        {
            "id": recipe.id,
            "title": recipe.title,
            "category": recipe.category,
            "ingredients": recipe.ingredients,
            "preparation": recipe.preparation,
            "created_at": recipe.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for recipe in recipes
    ]

    return jsonify({"recipes": recipes_json})

# ERROR HANDLING - Benutzerfreundliche Fehlerseiten
@views.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@views.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500