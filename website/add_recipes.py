from website import db
from website.models import Recipe

def add_sample_recipes():
    # Fügt Beispielrezepte zur Datenbank hinzu, falls noch keine vorhanden sind.
    # Falls bereits Rezepte existieren, wird kein weiteres Hinzufügen durchgeführt.

    # Überprüfung, ob bereits Rezepte in der Datenbank existieren
    if Recipe.query.first():
        print("Die Datenbank enthält bereits Rezepte. Kein erneutes Hinzufuegen noetig.")
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
        },
        {
        "title": "Lasagne Bolognese",
        "ingredients": "500g Hackfleisch, 1 Dose Tomaten, 1 Zwiebel, 2 Knoblauchzehen, 200g Lasagneplatten, 100g Parmesan, 200ml Béchamelsauce",
        "preparation": "Hackfleisch mit Zwiebeln und Knoblauch anbraten. Tomaten hinzufügen und köcheln lassen. Schichten mit Lasagneplatten und Béchamelsauce, dann backen.",
        "category": "Fleisch",
        },
        {
        "title": "Tomatensuppe",
        "ingredients": "500g Tomaten, 1 Zwiebel, 2 Knoblauchzehen, 500ml Gemüsebrühe, 2 EL Olivenöl, Salz, Pfeffer, Basilikum",
        "preparation": "Tomaten, Zwiebeln und Knoblauch anbraten, mit Brühe aufgießen und pürieren. Mit Salz, Pfeffer und Basilikum würzen.",
        "category": "Suppen",
        },
        {
        "title": "Hähnchen-Curry",
        "ingredients": "400g Hähnchenbrust, 1 Dose Kokosmilch, 2 TL Currypulver, 1 Zwiebel, 1 Paprika, Salz, Pfeffer",
        "preparation": "Hähnchen mit Zwiebeln und Paprika anbraten, Currypulver und Kokosmilch hinzufügen und köcheln lassen.",
        "category": "Fleisch",
        },
        {
        "title": "Gemüsepfanne",
        "ingredients": "1 Zucchini, 1 Paprika, 1 Karotte, 1 Zwiebel, 2 EL Sojasauce, 1 TL Sesamöl",
        "preparation": "Gemüse klein schneiden, in Sesamöl anbraten, mit Sojasauce würzen.",
        "category": "Vegetarisch",
        },
        {
        "title": "Eiersalat",
        "ingredients": "4 Eier, 2 EL Mayonnaise, 1 TL Senf, 1 EL Joghurt, Salz, Pfeffer, Schnittlauch",
        "preparation": "Eier kochen, hacken und mit den restlichen Zutaten vermengen.",
        "category": "Salate",
        },
        {
        "title": "Zitronenkuchen",
        "ingredients": "250g Mehl, 200g Zucker, 3 Eier, 1 Zitrone, 150g Butter, 1 TL Backpulver",
        "preparation": "Alle Zutaten verrühren, in eine Backform füllen und bei 180°C ca. 40 Minuten backen.",
        "category": "Nachtisch",
        },
        {
        "title": "Ratatouille",
        "ingredients": "1 Zucchini, 1 Aubergine, 1 Paprika, 2 Tomaten, 1 Zwiebel, 2 Knoblauchzehen, 2 EL Olivenöl",
        "preparation": "Gemüse in Würfel schneiden, in Olivenöl anbraten und köcheln lassen.",
        "category": "Vegetarisch",
        },
        {
        "title": "Schnitzel Wiener Art",
        "ingredients": "2 Schweineschnitzel, 1 Ei, 100g Mehl, 100g Paniermehl, Salz, Pfeffer, Öl",
        "preparation": "Schnitzel würzen, panieren und in heißem Öl goldbraun braten.",
        "category": "Fleisch",
        },
        {
        "title": "Kartoffelsuppe",
        "ingredients": "500g Kartoffeln, 1 Zwiebel, 1 Karotte, 1L Gemüsebrühe, Salz, Pfeffer",
        "preparation": "Kartoffeln und Gemüse würfeln, in Brühe kochen und pürieren.",
        "category": "Suppen",
        },
        {
        "title": "Apfelstrudel",
        "ingredients": "2 Äpfel, 50g Zucker, 1 TL Zimt, 1 Blätterteig, 50g Rosinen",
        "preparation": "Äpfel mit Zucker und Zimt mischen, in Blätterteig rollen und backen.",
        "category": "Nachtisch",
        },
        {
        "title": "Fischfilet mit Gemüse",
        "ingredients": "2 Fischfilets, 1 Zucchini, 1 Karotte, 1 Zwiebel, 1 EL Olivenöl, Salz, Pfeffer",
        "preparation": "Fisch würzen, mit Gemüse in Olivenöl anbraten und servieren.",
        "category": "Fisch",
        },
        {
        "title": "Linsensuppe",
        "ingredients": "200g Linsen, 1 Karotte, 1 Zwiebel, 1L Gemüsebrühe, Salz, Pfeffer, Kreuzkümmel",
        "preparation": "Linsen mit Gemüse in Brühe kochen und würzen.",
        "category": "Suppen",
        },
        {
        "title": "Hähnchenbrust mit Honig-Senf-Sauce",
        "ingredients": "2 Hähnchenbrüste, 2 EL Honig, 1 EL Senf, 100ml Sahne, Salz, Pfeffer",
        "preparation": "Hähnchenbrüste anbraten, Honig-Senf-Sauce dazugeben und köcheln lassen.",
        "category": "Fleisch",
        },
        {
        "title": "Gnocchi mit Gorgonzola-Sauce",
        "ingredients": "500g Gnocchi, 150g Gorgonzola, 200ml Sahne, 1 Knoblauchzehe, 1 TL Butter, Salz, Pfeffer",
        "preparation": "Gnocchi kochen. Gorgonzola in Sahne schmelzen, Knoblauch dazugeben und würzen. Gnocchi in die Sauce geben und servieren.",
        "category": "Vegetarisch",
        },
        {
        "title": "Mousse au Chocolat",
        "ingredients": "200g Zartbitterschokolade, 3 Eier, 50g Zucker, 200ml Sahne",
        "preparation": "Schokolade schmelzen. Eier trennen, Eiweiß steif schlagen. Eigelb mit Zucker verrühren, Schokolade unterheben. Sahne schlagen und alles vorsichtig mischen. Kühl stellen.",
        "category": "Nachtisch",
        }
    ]

    # Die Rezeptdaten in die Datenbank einfügen
    for data in recipes:
        new_recipe = Recipe(**data)  # Erstellen eines neuen Rezept-Objekts
        db.session.add(new_recipe)  # Hinzufügen zur Datenbank-Session

    # Änderungen in der Datenbank speichern
    db.session.commit()
    print("Beispielrezepte erfolgreich hinzugefuegt!")
