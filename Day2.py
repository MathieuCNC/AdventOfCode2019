#!/usr/bin/python2.7
#-*-coding:Utf-8 -*
inputFile = open("inputDay2.txt", "r")
content = inputFile.read()
intcode = [int(s) for s in content.split(",")]
print(intcode)
inputFile.close()

# Converting assist program to 1202 program

def gravityAssist(ic, noun, verb):
	ic[1] = noun
	ic[2] = verb

	for el in enumerate(ic):
		if el[0] % 4 == 0:
			if el[1] == 1: # Addition
				ic[ic[el[0]+3]] = ic[ic[el[0]+1]] + ic[ic[el[0]+2]]
			elif el[1] == 2:
				ic[ic[el[0]+3]] = ic[ic[el[0]+1]] * ic[ic[el[0]+2]]
			elif el[1] == 99:
				#print("Code 99: halting")
				break
			else:
				print("Wrong code: ", el[1])
		else:
			continue
	return ic[0]

i = 0
j = 0
while i < 100:
	while j < 100:
		if gravityAssist(list(intcode), i, j) == 19690720:
			print("Found noun and verb for 19690720: noun = {} and verb = {}".format(i, j))
			break
		j += 1
	i += 1
	j = 0


