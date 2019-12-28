#!/usr/bin/python2.7
#-*-coding:Utf-8 -*
numerateur = input("Saisissez un numérateur:")
denominateur = input("Saisissez un dénominateur:")
try:
	assert numerateur > 0
	if denominateur < 0:
		raise ValueError("Le denominateur est négatif")
	print("Division num / denom: ", numerateur / denominateur)
except NameError:
	print("Numerateur ou denominateur n\'a pas été définie")
except TypeError:
	#print("Numerateur ou denominateur n\'est pas compatible avec la division")
	pass # permet de ne rien faire
except ZeroDivisionError as messageOfException:
	print("Attention: division par 0!", messageOfException)
finally:
	print("Exécuté qu\'il y ait des erreurs ou non")
