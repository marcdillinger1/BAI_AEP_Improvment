# Improvement Task - Anwendungsentwicklung mit Python (AEP)

## Business Artificial Intelligence (BAI) - FHNW FS 2024

Dies ist das GitHub Repository welches die Pizza-Python-Applikation enthält, welche ich, Marc Dillinger, im Rahmen des Improvements im Modul Anwendungsentwicklung mit Python erarbeitet habe. 

### Aufgabenstellung: 

#### Bedingungen: 

Durch das erfolgreiche Lösen der folgenden Aufgaben können Studierende, die mit einer Note von 3.5 ungenügend dieses Modul abgeschlossen haben, die Note auf maximal 4.0 anheben. Falls die Aufgaben nicht erfolgreich und durch individuelle Eigenleistung gelöst werden, muss das komplette Modul wiederholt werden.

- Die Studierenden müssen die Aufgabe individuell und allein lösen.
- Die Studierenden dürfen keinen automatisch generierten Code verwenden. Die Lösung muss die individuellen Programmierfähigkeiten und die Anwendung der grundlegenden Konzepte widerspiegeln.
- Die Studierenden können auf Unterrichtsmaterialien und Übungen zurückgreifen, die während des Moduls bereitgestellt wurden.
- Die Studierenden können Teile des Projekts aus dem Modul wiederverwenden.
- Die Studierenden können SQLite/sqlalchemy oder eine Fake-Datenbank verwenden.
- Die Studierenden müssen alle Teilaufgaben bis zu der vereinbarten Frist vollständig abliefern. Das Versäumen dieser Frist führt zu einer ungenügenden Note.
- Änderungen an den Lösungen der Teilaufgaben nach Ablauf der Frist werden nicht akzeptiert.

#### Aufgaben:

- Erstelle ein neues Projekt verknüpft mit einem GitHub Repository. Dabei soll ein interaktives Python Programm erstellt werden, welches folgende Funktionalitäten implementiert:
- Erstelle eine eigene Pizza Klasse und treffe Annahmen, welche Eigenschaften und Methoden diese Klasse benötigt.
- Erstelle eine Liste oder eine Datenbank, welche Details verschiedener Pizzen pflegt.
- Erstelle die Funktionalität, die alle Pizzen mit ihren Belägen und allen anderen Details auflistet.
- Erstelle die Funktionalität, die nur Pizzen und deren Details mit den eingegebenen Belägen auflistet.
- Erstelle die Funktionalität, die den Benutzer eine Pizza über den Namen auswählen lässt und informiert, wenn der Name einer nicht verfügbaren Pizza eingegeben wurde.
- Erstelle die Funktionalität, die den Preis der ausgewählten Pizza anzeigt. Benutzer mit dem Gutscheincode „PIZZA10“ erhalten 10% Rabatt.
- Erstelle ein kurzes Video (max. 10 Minuten), in welchem du das laufende Programm demonstrierst und Code-Ausschnitte mit den angewendeten Konzepten erläuterst. Veröffentliche das Video auf Switch Tube.

#### Deliverables: 

Lade bis zu der vereinbarten Frist im Moodle die folgenden Informationen hoch:

- Link zum GitHub Repository, mit Zugriff für die Dozierenden.
- Link zum Video (keine Datei), mit Zugriff für die Dozierenden.

#### Dozierende:

Charuta Pande (charuta.pande@fhnw.ch, GitHub: charutapande)

Phillip Gachnang (phillip.gachnang@fhnw.ch, GitHub: PhillipGachnangFHNW)

### Anwendung

Die Anwendung wird im `main.py` ausgeführt und wird vom User durch die einfache Benutzeroberfläche bedient.
Der User hat 5 Optionen, welche es ihm ermöglichen, die geforderten Aktionen ausführen zu können.

1. show pizza menu - zum Anzeigen des kompletten Menus

2. search pizzas with specific topping(s) - zum suchen von Pizzen mit bestimmten Toppings

3. select a pizza by name - zum Auswählen einer Pizza durch Eingabe des Namens

4. apply discount code / calculate price - zum Anwenden eines Rabattcodes und der berechnung des Preises einer ausgewählten Pizza

5. end application - zum beenden der Applikation

### Aufbau 

Die Python-Applikation ist in 3 Files aufgeteilt welche alle ihren eigenen Zweck erfüllen.

`main.py` - Sorgt für die Benutzeroberfläche und die Ausführung des Programmes

`database.py` - agiert als Datenbank und beinhaltet die Liste aller Pizza-Objekte und deren Informationen (Name, Toppings und Preis) inklusive wichtiger Funktionen wie `pizza_menu` zum anzeigen des Pizza Menu, `show_pizza_with_toppings` zum Suchen von Pizzen mit bestimmten Topping(s) und `show_pizza_with_name` um Pizzen anhand des Namens anzeigen zu können

`pizza.py` - beinhaltet den Konstruktor der Pizza Klasse und die Funktion `pizza_informations` welche dafür sorgt die Informationen der Pizzen anzeigen zu können
