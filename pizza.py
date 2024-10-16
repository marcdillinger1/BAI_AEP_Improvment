class Pizza:

    #Bauplan/Konstruktor Pizza Klasse

    def __init__(self, name, topping, price):
        self.name = name
        self.topping = topping
        self.price = price

#Funktion Informationen der Pizza anzeigen
    def pizza_informations(self):
        return f"{self.name} - {', '.join(self.topping)} - {self.price:.2f} CHF"

#Funktion überprüfen der Pizzen nach Toppings

    def has_topping(self, topping):
        return topping in self.topping