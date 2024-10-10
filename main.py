from database import pizza_menu, show_pizza_with_topping, show_pizza_with_name

def main():
    while True:
        print("1 - show pizza menu")
        print("2 - show pizzas with a specific topping")
        print("3 - chose a pizza by name")
        print("4 - use discount code")
        print("5 - end application")
        choice = input("Chose Option:")

        if choice == "1":

        elif choice == '2':

        elif choice == '3':

        elif choice == '4':

        elif choice == '5':
            print("closing the application")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()