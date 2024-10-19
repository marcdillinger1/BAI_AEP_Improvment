# Importiert die Pizza Klasse aus dem pizza.py File
from pizza import Pizza

# Pizza Menu (Datenbank)
# eine Liste von allen verfügbaren Pizzen (Pizza Objekten) mit Ihren Eigenschaften (Name, Toppings-Liste, Preis)
pizzas = [
    Pizza("margherita", ["tomato", "mozzarella"], 10.00),
    Pizza("hawaii", ["tomato", "mozzarella", "pineapple", "ham"], 14.00),
    Pizza("salami", ["tomato", "mozzarella", "salami"], 12.00),
    Pizza("diavola", ["tomato", "mozzarella", "salami", "onions", "chilies"], 14.00),
    Pizza("prosciutto", ["tomato", "mozzarella", "ham"], 12.00),
    Pizza("parma", ["tomato", "mozzarella", "parma ham", "rucola", "parmesan cheese"], 18.00),
    Pizza("tonno", ["tomato", "mozzarella", "tuna"], 14.00),
    Pizza("funghi", ["tomato", "mozzarella", "mushrooms"], 14.00),
    Pizza("prosciutto funghi", ["tomato", "mozzarella", "ham", "mushrooms"], 16.00),
    Pizza("tonno cipolla", ["tomato", "mozzarella", "tuna", "onions"], 16.00)
]

# Funktion um das gesamte Pizza-Menu anzuzeigen
# zeigt alle Pizzen in einer Liste formatierter strings an,
# indem die Methode pizza_informations aus pizza.py für jedes Pizza-Objekt angewendet wird
def pizza_menu():
    return [pizza.pizza_informations() for pizza in pizzas]

# Funktion um Pizzen mit bestimmten Toppings anzuzeigen
# nimmt eine durch Kommas getrennte Liste von Toppings als Eingabe
def show_pizza_with_toppings (toppings):
    # Teilt die Eingabe in eine Liste von Toppings auf
    topping_list = toppings.split(",")
    # Entfernt Leerzeichen (strip()) und wandelt alle Toppings in Kleinbuchstaben (lower()) um damit Gross-/Kleinschreibung und Leerzeichen keine Probleme verursachen
    topping_list = [topping.strip().lower() for topping in topping_list]
    # Durchläuft die Liste aller Pizzen und prüft jede Pizza, ob sie alle (all()) angefragten Toppings enthält
    # und gibt dann eine Liste der Pizzen mit ihren Informationen (pizza_informations aus pizza.py) zurück welche die gesuchten Toppings enthalten
    return [pizza.pizza_informations() for pizza in pizzas if all(topping in pizza.toppings for topping in topping_list)]

# Funktion zur Suche einer bestimmten Pizza anhand des Namens
def show_pizza_with_name (name):
    # Durchsucht jedes Pizza-Objekt in der Liste Pizzas
    for pizza in pizzas:
        # prüft, ob die Namen der gesuchten Pizza und dem Pizza-Objekt übereinstimmen
        if pizza.name == name:
            # gibt die Pizza zurück, wenn die Namen übereinstimmen
            return pizza
    # gibt none zurück, wenn keine pizza mit dem Namen gefunden wurde
    return None
