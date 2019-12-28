#!/usr/bin/python2.7
#-*-coding:Utf-8 -*
myFile = open("inputDay1.txt", "r")
content = myFile.read()
inputList = content.split("\n")
inputList = [int(s) for s in inputList if len(s) != 0]

print("Start of computation. Length: ", len(inputList))
totalFuel = 0
for el in inputList:
	fuel = 0
	while el > 0:
		el = el // 3 - 2
		if el > 0:
			fuel += el
			totalFuel += el
	#print("Masse: {} - Fuel: {}".format(el, fuel))

print("Result: ", totalFuel)

myFile.close()
