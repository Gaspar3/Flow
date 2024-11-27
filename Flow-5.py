def erstellen(name1, name2, name3):
    tuple = (name1, name2, name3)
    return tuple
def uberpruffen(liste,suche):
    if suche in liste:
        print("Buch gefunden")
    else:
        print("Buch nicht gefunden")

name1 = input("Gebe den ersten Buchnamen ein: ")
name2 = input("Gebe den zweiten Buchnamen ein: ")
name3 = input("Gebe den letzen Buchnamen ein: ")

liste = erstellen(name1,name2,name3)
print(liste[0])
print(liste[1])
print(liste[2])

x = input("Welches buch möchtest du suchen? ")
uberpruffen(liste,x)
