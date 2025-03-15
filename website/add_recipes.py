from website import db
from website.models import Recipe

def add_sample_recipes():
    if Recipe.query.first():
        print("📌 Die Datenbank enthält bereits Rezepte. Kein erneutes Hinzufügen nötig.")
        return

    recipes = [
        {
            "title": "Spaghetti Carbonara",
            "ingredients": "200g Spaghetti, 100g Speck, 2 Eier, 50g Parmesan, 1 TL Pfeffer, 1 Prise Salz",
            "preparation": "Spaghetti in Salzwasser kochen. Speck anbraten. Eier mit Parmesan verquirlen. Alles mischen und mit Pfeffer würzen.",
            "category": "Fleisch",
        },
        {
            "title": "Vegetarisches Chili",
            "ingredients": "1 Dose Kidneybohnen, 1 rote Paprika, 2 Tomaten, 1 Zwiebel, 2 Knoblauchzehen, 1 TL Kreuzkümmel, 1 TL Chilipulver",
            "preparation": "Zwiebeln und Knoblauch anbraten. Paprika hinzufügen und kurz mitbraten. Tomaten und Bohnen dazugeben und köcheln lassen.",
            "category": "Vegetarisch",
        },
        {
            "title": "Pfannkuchen",
            "ingredients": "200g Mehl, 300ml Milch, 2 Eier, 1 EL Zucker, 1 Prise Salz, Butter zum Braten",
            "preparation": "Alle Zutaten zu einem glatten Teig verrühren. Etwas Butter in einer Pfanne erhitzen und den Teig portionsweise ausbacken.",
            "category": "Süßspeisen",
        },
        {
            "title": "Griechischer Salat",
            "ingredients": "1 Gurke, 2 Tomaten, 100g Feta-Käse, 1 rote Zwiebel, 50g Oliven, 2 EL Olivenöl, 1 TL Oregano",
            "preparation": "Gurke, Tomaten, Feta und Zwiebel in Stücke schneiden. Mit Oliven, Olivenöl und Oregano vermengen.",
            "category": "Salate",
        }
    ]

    for data in recipes:
        new_recipe = Recipe(**data)
        db.session.add(new_recipe)

    db.session.commit()
    print("✅ Beispielrezepte erfolgreich hinzugefügt!")
