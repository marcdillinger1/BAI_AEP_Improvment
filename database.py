from pizza import Pizza

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

#Funktion um das gesamte Pizza-Menu anzuzeigen

def pizza_menu():
    return [pizza.pizza_informations() for pizza in pizzas]

#Funktion um Pizzen mit bestimmten Toppings anzuzeigen

def show_pizza_with_toppings (toppings):
    topping_list = toppings.split(",")
    topping_list = [topping.strip().lower() for topping in topping_list]
    return [pizza.pizza_informations() for pizza in pizzas if all(topping in pizza.toppings for topping in topping_list)]

#Funktion um eine Pizza mit einem bestimmten Namen anzuzeigen

def show_pizza_with_name (name):
    for pizza in pizzas:
        if pizza.name == name:
            return pizza
    return None
