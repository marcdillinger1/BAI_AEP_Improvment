# Die Pizza-Klasse repräsentiert eine Pizza mit ihren Eigenschaften
class Pizza:
    # Konstruktor der Pizza-Klasse, der die Eigenschaften einer Pizza initialisiert.
    def __init__(self, name, toppings, price):
        # name (string) - der Name der Pizza
        # topping (list) - eine Liste mit den Toppings der Pizza
        # price (float) - der Preis der Pizza
        self.name = name
        self.toppings = toppings
        self.price = price

    # Funktion die Informationen der Pizza als formatierten string zurückgibt mit:
    # Dem Namen der Pizza
    # einer Liste der Toppings getrennt durch ein Komma
    # der Preis der Pizza formatiert mit 2 Nachkommastellen (.2f) und der Währung CHF
    def pizza_informations(self):
        return f"{self.name} - {', '.join(self.toppings)} - {self.price:.2f} CHF"
