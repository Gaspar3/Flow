data = {
    "Gaspar Balo": "121879580",
    "Lennard Schock": "7385635578"
}

def auslesen(dict_obj):
    """Liest das Dictionary aus und gibt die Namen und Nummern aus."""
    for key, value in dict_obj.items():
        print(f"{key} hat die Nummer {value}")

def hinzufügen(name, nummer, dict_obj):
    """Fügt eine neue Person und Nummer dem Dictionary hinzu."""
    dict_obj[name] = nummer
    print(f"Person {name} erfolgreich hinzugefügt.")

def loschen(name, dict_obj):
    """Löscht eine Person aus dem Dictionary."""
    if dict_obj.pop(name, None):
        print(f"Person {name} erfolgreich gelöscht.")
    else:
        print(f"Person {name} nicht gefunden.")

while True:
    wahl = input("""
Was möchtest du machen?
1: Auslesen
2: Hinzufügen
3: Löschen
4: Beenden
Deine Wahl: """)

    if wahl == "1":
        auslesen(data)
    elif wahl == "2":
        name = input("Wie heißt die Person? ")
        nummer = input("Welche Nummer hat diese Person? ")
        hinzufügen(name, nummer, data)
    elif wahl == "3":
        name = input("Welche Person möchtest du löschen? ")
        loschen(name, data)
    elif wahl == "4":
        print("Programm beendet.")
        break
    else:
        print("Ungültige Eingabe. Bitte wähle eine gültige Option.")
