#!/usr/local/bin/python3
#-*-coding:Utf-8 -*
#print("ddd", end="")

with open("inputDay4.txt", "r") as inputFile :
	content = inputFile.read()
	r = content.split("-")
	print(content, r)

def increasingNb(digits):
	compliant = True
	for i, d in enumerate(digits):
		if i > 0:
			if d < digits[i-1]:
				compliant = False
				break
	return compliant

def hasTwin(digits):
	compliant = False
	i = 1
	while i < len(digits):
		j = i
		cardG = 1
		while j < len(digits) and digits[j] == digits[i-1]:
			cardG += 1
			j += 1
		if cardG == 2:
			compliant = True
			break
		elif cardG > 1:
			i = j
		else:
			i += 1
	return compliant

nbCompliantCodes = 0
listCompliantCodes = []
for el in range(int(r[0]), int(r[1])):
	digits = [int(nb) for nb in str(el)]
	if increasingNb(digits) and hasTwin(digits):
		nbCompliantCodes += 1
		listCompliantCodes.append(el)

print("Result: nbCompliantCodes {} list {}".format(nbCompliantCodes, ""))