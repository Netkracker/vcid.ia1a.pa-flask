from website import db
from website.models import Recipe

def add_sample_recipes():
    # Fügt Beispielrezepte zur Datenbank hinzu, falls noch keine vorhanden sind.
    # Falls bereits Rezepte existieren, wird kein weiteres Hinzufügen durchgeführt.

    # Überprüfung, ob bereits Rezepte in der Datenbank existieren
    if Recipe.query.first():
        print("Die Datenbank enthält bereits Rezepte. Kein erneutes Hinzufügen nötig.")
        return

    # Liste mit Beispielrezepten
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
            "category": "Nachtisch",
        },
        {
            "title": "Tacos mit Hackfleisch",
            "ingredients": "250g Hackfleisch, 1 kleine Zwiebel, 1 Tomate, 1 TL Paprikapulver, 1 TL Kreuzkümmel, 4 Taco-Schalen, 50g geriebener Käse",
            "preparation": "Zwiebel fein hacken und mit Hackfleisch anbraten. Tomate würfeln und mit den Gewürzen hinzufügen. Die Mischung in Taco-Schalen füllen, mit Käse bestreuen und servieren.",
            "category": "Fleisch",
        },
        {
            "title": "Schoko-Brownies",
            "ingredients": "200g Zartbitterschokolade, 150g Butter, 150g Zucker, 3 Eier, 100g Mehl, 1 TL Backpulver",
            "preparation": "Schokolade und Butter schmelzen. Zucker und Eier schaumig schlagen, dann die geschmolzene Schokolade einrühren. Mehl und Backpulver unterheben. In eine Backform geben und bei 180°C ca. 25 Minuten backen.",
            "category": "Nachtisch",
        }
    ]

    # Die Rezeptdaten in die Datenbank einfügen
    for data in recipes:
        new_recipe = Recipe(**data)  # Erstellen eines neuen Rezept-Objekts
        db.session.add(new_recipe)  # Hinzufügen zur Datenbank-Session

    # Änderungen in der Datenbank speichern
    db.session.commit()
    print("Beispielrezepte erfolgreich hinzugefügt!")
