#!/usr/local/bin/python3
#-*-coding:Utf-8 -*
with open("inputDay5.txt", "r") as inputFile:
	content = inputFile.read()
	intcode = [int(s) for s in content.split(",")]
	#print(intcode)
	inputFile.close()

def testDiagnostic(ic):
	index = 0
	indexLeap = 100
	isLeap = True
	while indexLeap != 0:
		indexLeap, isLeap = runInstruction(ic, index)
		if isLeap == True:
			index += indexLeap
		else:
			index = indexLeap


def runInstruction(ic, index):

	# commande
	com = str(ic[index])
	opcode = com[len(com)-2:]
	indexLeap = int()
	isLeap = True

	# Compute leap and fn
	nbOpcode = int(opcode)
	if nbOpcode in [1, 2, 7, 8]:
		indexLeap = 4
		if nbOpcode == 1:
			fn = addFn
		elif nbOpcode == 2:
			fn = multiplyFn
		elif nbOpcode == 7:
			fn = lessFn
		else:
			fn = equalFn
	elif nbOpcode in [3, 4]:
		indexLeap = 2
	elif nbOpcode in [5, 6]:
		indexLeap = 3
		if nbOpcode == 5:
			fn = jumpIfTrueFn
		else:
			fn = jumpIfFalseFn
	elif nbOpcode == 99:
		indexLeap = 0
		print("Program halting: opcode 99")
	else:
		print("Wrong opcode: {}".format(nbOpcode))
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
		if nbOpcode in [1, 2, 7, 8]:
			fn(param[0], param[1], param[2], ic)
		elif nbOpcode == 3:
			inputFn(5, param[0], ic)
		elif nbOpcode == 4:
			outputFn(param[0], ic)
		elif nbOpcode in [5, 6]:
			leap = fn(param[0], param[1], ic)
			print("Leap = {}".format(leap))
			if leap is not None:
				indexLeap = leap
				isLeap = False
			print("indexLeap = {}".format(indexLeap))
	#except IndexError as messageError:
	#	print("IndexError: Com {} param {} message {}".format(com, ", ".join(param), messageError))

	return indexLeap, isLeap

def addFn(a, b, saveIndex, intcode):
	intcode[saveIndex] = intcode[a] + intcode[b]

def multiplyFn(a, b, saveIndex, intcode):
	intcode[saveIndex] = intcode[a] * intcode[b]

def inputFn(inputValue, saveIndex, intcode):
	intcode[saveIndex] = inputValue

def outputFn(indexToOutput, intcode):
	print("Output at index {}: {}".format(str(indexToOutput), str(intcode[indexToOutput])))

def lessFn(a, b, saveIndex, intcode):
	if intcode[a] < intcode[b]:
		intcode[saveIndex] = 1
	else:
		intcode[saveIndex] = 0

def equalFn(a, b, saveIndex, intcode):
	#print(a, b, saveIndex)
	if intcode[a] == intcode[b]:
		intcode[saveIndex] = 1
	else:
		intcode[saveIndex] = 0

def jumpIfTrueFn(a, b, intcode):
	result = None
	if intcode[a] != 0:
		result = intcode[b]
	return result

def jumpIfFalseFn(a, b, intcode):
	result = None
	if intcode[a] == 0:
		result = intcode[b]
	return result

# Launch Test
testDiagnostic(intcode)
