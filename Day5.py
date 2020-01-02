#!/usr/local/bin/python3
#-*-coding:Utf-8 -*
with open("inputDay5.txt", "r") as inputFile:
	content = inputFile.read()
	intcode = [int(s) for s in content.split(",")]
	#print(intcode)
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

def testDiagnostic(ic):
	# 1202 program alarm
	#ic[1] = 12
	#ic[2] = 2

	index = 0
	indexLeap = 100
	while indexLeap != 0:
		indexLeap = runInstruction(ic, index)
		index += indexLeap


def runInstruction(ic, index):

	# commande
	com = str(ic[index])
	opcode = com[len(com)-2:]
	indexLeap = int()
	

	# Compute leap and fn
	nbOpcode = int(opcode)
	if nbOpcode in [1, 2]:
		indexLeap = 4
		if nbOpcode == 1:
			fn = addFn
		else:
			fn = multiplyFn
	elif nbOpcode in [3, 4]:
		indexLeap = 2
	elif nbOpcode == 99:
		indexLeap = 0
		print("Program halting: opcode 99")
	else:
		print(ic)
		raise ValueError("Unknown opcode {}, com {}, index {}".format(opcode, com, index))

	#try:
	if opcode != "99":
		# Get parameters
		param = list()
		for i in range(1, indexLeap):
			try:
				mode = com[-2-i]
			except IndexError as iemessage:
				mode = '0'
			if mode == '0':# position mode
				param.append(ic[index+i]);
			elif mode == '1':# immediate mode
				param.append(index+i)
			else:
				print("Attention erreur!")

		# Run instruction
		#print(ic)
		#print("Run instruction opcode {} param {}, {}, {} and index {}".format(opcode, ic[index+1], ic[index+2], ic[index+3], index))
		#print("Param {}".format(", ".join([str(el) for el in param])))
		if nbOpcode in [1, 2]:
			fn(param[0], param[1], ic, param[2])
		elif nbOpcode == 3:
			inputFn(1, ic, param[0])
		elif nbOpcode == 4:
			outputFn(ic, param[0])
	#except IndexError as messageError:
	#	print("IndexError: Com {} param {} message {}".format(com, ", ".join(param), messageError))

	return indexLeap

def addFn(a, b, intcode, saveIndex):
	intcode[saveIndex] = intcode[a] + intcode[b]

def multiplyFn(a, b, intcode, saveIndex):
	intcode[saveIndex] = intcode[a] * intcode[b]

def inputFn(inputValue, intcode, saveIndex):
	intcode[saveIndex] = inputValue

def outputFn(intcode, indexToOutput):
	print("Output at index {}: {}".format(indexToOutput, intcode[indexToOutput]))


# Launch Test
testDiagnostic(intcode)
