#!/usr/bin/python2.7
#-*-coding:Utf-8 -*
minuscules = "chaine en minuscule"
print("upper: ", minuscules.upper())
print("capitalize: ", minuscules.capitalize())
espace = "    chaine avec espaces    "
print("strip: ", espace.strip())
titre = "introduction"
titre.upper().center(20)
print("Je m\'appelle {0} {1} et j\'ai {2} ans (pour l\'admin {0})".format("Louis", "XIV", 25, "Louis".upper()))
print("Je mappelle {} {} et jai {} ans".format("Louis", "XIV", 25))
print("Je mappelle {prenom} {nom} et jai {age} ans".format(prenom="Louis", nom="XIV", age=25))

#Chaine de caractères
chaine = "hello there!"
chaine[0:2]
chaine[:2]
chaine[2:]

# Liste
liste = list()
liste = [1, 3, 7]
liste.append(8)
liste.insert(1, 9)
del liste[0]
liste.remove(3)
liste.extend([0, 0])
liste += [10]
print("Liste: ", liste)
for el in liste:
	print(el)
for i, el in enumerate(liste):
	print("L\'élément d\'index {} est {}".format(i, el))
for el in enumerate(liste):
	print("Tuple: ", el, " - Index: ", el[0], " - Valeur: ", el[1])

#Tuple: liste non modifiable
tup = ()
tup = (1,)
tup = 1,
tup = (1, 2, 5)
print("Tuple: ", tup)

# Fonction à nb de paramètres inconnu
def fonction_inconnue(*param):
	print("J\'ai reçu: {}".format(param))
def fonction_inconnue2(nom, prenom, *param):
	print(nom, prenom, param)

# Passer les el d'une liste en param
liste = [1, 5, 7, 9]
print("Liste: ", liste) # affiche la liste
#print(*liste) # affiche comme si print(1, 5, 7, 9)

# Compréhensions de liste (comme les maps)
liste_carre = [nb * nb for nb in liste]
print("Liste au carré: ", liste_carre)

# Filtrage de liste
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("[nb for nb in liste if nb % 2 == 0]: ", [nb for nb in liste if nb % 2 == 0])
