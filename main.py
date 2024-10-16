from database import pizza_menu, show_pizza_with_topping, show_pizza_with_name

def main():
    while True:
        print("1 - show pizza menu")
        print("2 - show pizzas with a specific topping")
        print("3 - chose a pizza by name")
        print("4 - use discount code")
        print("5 - end application")
        choice = input("Chose Option:")

        if choice == '1':
            pizzas = pizza_menu()
            print ("Pizza Menu:")
            for pizza in pizzas:
                print(pizza)

        elif choice == '2':
            topping = input("Please enter the topping you want to search for:").lower()
            pizzas = show_pizza_with_topping(topping)
            if pizzas:
                print ("Pizzas with topping:", topping, ":")
                for pizza in pizzas:
                    print(pizza)
            else:
                print("No pizzas with specified topping")

        elif choice == '3':
            name = input("Please enter the name of the pizza you want to choose:").lower()
            pizza = show_pizza_with_name(name)
            if pizza:
                print("Selected Pizza:")
                print(pizza.pizza_informations())
            else:
                print("no Pizza found :(")

        elif choice == '4':
            name = input("Please enter the name of the pizza you want to calculate your discounted price:").lower()
            pizza = show_pizza_with_name(name)
            if pizza:
                discount_code = input("Please enter your discount code or press enter to skip:")
                if discount_code == "PIZZA10":
                    discounted_price = pizza.price * 0.9
                    print ("Discounted price:", discounted_price, "CHF")
                else:
                    print ("Price", pizza.price, "CHF")
            else:
                print("No pizza found :(")


        elif choice == '5':
            print("closing the application")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()