from pizza import Pizza

#Alle verfügbaren Pizzen aufgelistet (Datenbank)

pizzas = [
    Pizza("Margherita", ["tomato", "mozzarella"], 10.00),
    Pizza("Hawaii", ["tomato", "mozzarella", "pineapple", "ham"], 14.00),
    Pizza("Salami", ["tomato", "mozzarella", "salami"], 12.00),
    Pizza("Diavola", ["tomato", "mozzarella", "salami", "onions", "chilies"], 14.00),
    Pizza("Prosciutto", ["tomato", "mozzarella", "ham"], 12.00),
    Pizza("Parma", ["tomato", "mozzarella", "parma ham", "rucola", "parmesan cheese"], 18.00),
    Pizza("Tonno", ["tomato", "mozzarella", "tuna"], 14.00),
    Pizza("Funghi", ["tomato", "mozzarella", "mushrooms"], 14.00),
    Pizza("Prosciutto Funghi", ["tomato", "mozzarella", "ham", "mushrooms"], 16.00),
    Pizza("Tonno Cipolla", ["tomato", "mozzarella", "tuna", "onions"], 16.00)
]

#Funktion um das gesamte Pizza-Menu anzuzeigen

def pizza_menu():
    return [pizza.pizza_informations() for pizza in pizzas]

#Funktion um Pizzen mit bestimmten Toppings anzuzeigen

def show_pizza_with_topping (topping):
    return [pizza.pizza_informations() for pizza in pizzas if pizza.has_topping(topping)]

#Funktion um eine Pizza mit einem bestimmten Namen anzuzeigen

def show_pizza_with_name (name):
    for pizza in pizzas:
        if pizza.name == name:
            return pizza
    return None
