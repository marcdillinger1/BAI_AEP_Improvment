# Importiert die Funktionen aus database.py
# pizza_menu - Funktion zum anzeigen des gesamten Pizza Menu
# show_pizza_with_toppings - Funktion um Pizzen mit bestimmten Toppings anzuzeigen
# show_pizza_with_name - Funktion zur Suche einer bestimmten Pizza anhand des Namens
from database import pizza_menu, show_pizza_with_toppings, show_pizza_with_name

# Hauptfunktion der Appliaktion welche die Benutzeroberfläche steuert
def main():
    # Endlosschleife um das Hauptmenü anzuzeigen bis der User die Anwendung beendet
    while True:
        # Option 1 - Anzeigen des Pizza Menu
        print("1 - show pizza menu")
        # Option 2 - Suchen von Pizzas mit bestimmten Toppings
        print("2 - search pizzas with specific topping(s)")
        # Option 3 - Auswählen einer bestimmten Pizza nach Namen
        print("3 - select a pizza by name")
        # Option 4 - Berechnung des Preises und verwendung von Rabattcode
        print("4 - apply discount code / calculate price")
        # Option 5 - Anwendung Beenden
        print("5 - end application")
        # Aufforderung an den User eine Option auszuwählen
        choice = input("Chose Option:")

        # Option 1 - Anzeigen des Pizza Menu
        if choice == '1':
            # ruft die Funktion pizza_menu auf, um das gesamte Pizza Menu zu erhalten
            pizzas = pizza_menu()
            # gibt den Titel Pizza Menu aus
            print ("Pizza Menu:")
            # durchläuft jedes Pizza Objekt in der Pizza Liste
            for pizza in pizzas:
                # gibt jede Pizza mit ihren Informationen aus im Pizza Menu
                print(pizza)

        # Option 2 - Suchen von Pizzas mit bestimmten Toppings
        elif choice == '2':
            # Aufforderung an den User seine gewünschten Toppings einzugeben (getrennt mit einem Komma)
            # .lower() wandelt die gesamte Eingabe in Kleinbuchstaben um, um Fehler zu vermeiden
            topping = input("Please enter the topping(s) you want to search for (please seperate toppings with , ):").lower()
            # ruft die Funktion show_pizza_with_topping auf, um Pizzen mit den eingegebenen Toppings zu suchen
            pizzas = show_pizza_with_toppings(topping)
            # falls Pizzen mit den bestimmten Toppings gefunden wurden
            if pizzas:
                # Benachrichtigung, dass Pizzen mit den bestimmten Toppings gefunden wurden
                print ("Pizzas with topping(s):", topping, ":")
                # geht alle gefundenen Pizzen welche die bestimmten Toppings enthalten durch
                for pizza in pizzas:
                    # zeigt alle gefundenen Pizzen mit ihren Informationen dem User an
                    print(pizza)
            # falls keine Pizzen mit den bestimmten Toppings gefunden wurden
            else:
                # Benachrichtigung an User das keine Pizzen mit den bestimmten Toppings gefunden wurden
                print("No pizzas with specified topping(s) found")

        # Option 3 - Auswählen einer bestimmten Pizza nach Namen
        elif choice == '3':
            # Aufforderung an den User den Namen seiner gewünschten Pizza einzugeben
            # .lower() wandelt die gesamte Eingabe in Kleinbuchstaben um, um Fehler zu vermeiden
            name = input("Please enter the name of the pizza you want to select:").lower()
            # ruft die Funktion show_pizza_with_name auf, zur Suche einer Pizza anhand des Namens
            pizza = show_pizza_with_name(name)
            # falls eine Pizza mit dem bestimmten Namen gefunden wurde
            if pizza:
                # Benachrichtigung Pizza mit bestimmten namen gefunden
                print("Selected Pizza:")
                # zeigt die bestimmte ausgewählte Pizza mit all ihren Informationen (pizza_inforamtions) an
                print(pizza.pizza_informations())
            # falls keine Pizza mit dem bestimmten Namen gefunden wurde
            else:
                # Benachrichtigung an den User das keine Pizza mit dem bestimmten Namen gefunden wurde
                print("no Pizza found :(")

        # Option 4 - Berechnung des Preises und verwendung von Rabattcode
        elif choice == '4':
            # Aufforderung an den User den Namen seiner gewünschten Pizza einzugeben
            # .lower() wandelt die gesamte Eingabe in Kleinbuchstaben um, um Fehler zu vermeiden
            name = input("Please enter the name of the pizza you want to calculate your discounted price:").lower()
            # ruft die Funktion show_pizza_with_name auf, zur Suche einer Pizza anhand des Namens
            pizza = show_pizza_with_name(name)
            # falls eine Pizza gefunden wird welche der Eingabe entspricht
            if pizza:
                # Aufforderung an den User seinen Discount Code einzugeben oder mit enter zu überspringen
                discount_code = input("Please enter your discount code or press enter to skip:")
                # falls der Discount Code gültig ist (PIZZA10)
                if discount_code == "PIZZA10":
                    # berechnet den reduzierten preis welcher 90% vom ursprünglichen pizza.price beträgt (10% Rabatt)
                    discounted_price = pizza.price * 0.9
                    # Benachrichtigung an den User, dass der Rabattcode erfolgreich angewendet wurde
                    print("Discount code successfully applied")
                    # Benachrichtigung an den User mit dem reduzierten Preis (.2f 2 Nachkommastellen) in CHF
                    print(f"Discounted price: {discounted_price:.2f} CHF")
                # falls der Discount Code ungültig ist oder vom User übersprungen wurde
                else:
                    # Benachrichtigung an den User das kein oder ein ungültiger Discount Code angewendet wurde
                    print("None or invalid discount code")
                    # Benachrichtigung an den User mit dem regulären Preis (.2f 2 Nachkommastellen) in CHF
                    print(f"Regular price: {pizza.price:.2f} CHF")
            # falls keine Pizza gefunden wird welche der Eingabe entspricht
            else:
                # Benachrichtigung an den User das keine Pizza gefunden wurde
                print("No pizza found :(")

        # Option 5 - Anwendung Beenden
        elif choice == '5':
            # Benachrichtigung an den User das die Anwendung beendet wird
            print("Closing the application")
            # beendet Anwendung
            break

        # Ungültige Eingabeoption
        else:
            # Benachrichtigung an den User dass seine Eingabe ungültig war und er es nochmals versuchen soll
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()