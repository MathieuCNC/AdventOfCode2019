#!/usr/bin/python2.7
#-*-coding:Utf-8 -*

# Première manière d'instancier un dico
monDict = dict()
type(monDict)
# 2ème manière
montDict = {}
monDict["pseudo"] = "Prolixe"
monDict["mot de passe"] = "*"
monDict[0] = "a"

"""
Un dictionnaire est un objet conteneur associant des clés à des valeurs.

Pour créer un dictionnaire, on utilise la syntaxedictionnaire = {cle1:valeur1, cle2:valeur2, cleN:valeurN}.

On peut ajouter ou remplacer un élément dans un dictionnaire :dictionnaire[cle] = valeur.

On peut supprimer une clé (et sa valeur correspondante) dun dictionnaire en utilisant, au choix, le mot-clédelou la méthodepop.

On peut parcourir un dictionnaire grâce aux méthodeskeys(parcourt les clés),values(parcourt les valeurs) ouitems(parcourt les couples clé-valeur).

On peut capturer les paramètres nommés passés à une fonction en utilisant cette syntaxe :def fonction_inconnue(**parametres_nommes): (les paramètres nommés se retrouvent dans le dictionnaireparametres_nommes).