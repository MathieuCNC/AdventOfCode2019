#!/usr/bin/python2.7
# -*-coding:Utf-8 -*
print("Hello!")
year = input("Saisissez une année pour vérifier si elle est bisextile: ")
print(type(year))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): 
	print("L'année ", year, " est bisextile")
else:
	print("L'année ", year, " n'est pas bisextile")
