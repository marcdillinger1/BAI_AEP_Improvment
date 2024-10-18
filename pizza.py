class Pizza:

    def __init__(self, name, toppings, price):
        self.name = name
        self.toppings = toppings
        self.price = price

#Funktion Informationen der Pizza anzeigen
    def pizza_informations(self):
        return f"{self.name} - {', '.join(self.toppings)} - {self.price:.2f} CHF"

#Funktion überprüfen der Pizzen nach Toppings

    def has_topping(self, toppings):
        return toppings in self.toppings