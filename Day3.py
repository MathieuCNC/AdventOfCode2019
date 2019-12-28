#!/usr/bin/python3
#-*-coding:Utf-8 -*
import sys


with open("inputDay3.txt", "r") as inputFile:
	content = inputFile.read()
	wires = content.split("\n")
	w1 = wires[0].split(",")
	w2 = wires[1].split(",")
	print(w1, " - ", w2)


def runWire(grid, wire, wireId):
	# cursor position
	pos = [0, 0]
	totalStep = 0
	for i in wire:
		d = i[:1] # direction
		n = int(i[1:]) # number of steps
		count = 1;
		if d == 'R':
			while count <= n:
				pos[0] += 1
				totalStep += 1
				grid = setToGrid(grid, pos, d + wireId, totalStep)
				count += 1
		if d == 'L':
			while count <= n:
				pos[0] -= 1
				totalStep += 1
				grid = setToGrid(grid, pos, d + wireId, totalStep)
				count += 1
		if d == 'U':
			while count <= n:
				pos[1] += 1
				totalStep += 1
				grid = setToGrid(grid, pos, d + wireId, totalStep)
				count += 1
		if d == 'D':
			while count <= n:
				pos[1] -= 1
				totalStep += 1
				grid = setToGrid(grid, pos, d + wireId, totalStep)
				count += 1
		#print("Direction {} pos {}".format(i, pos))

	return grid
	
def setToGrid(grid, position, direction, step):
	tup = tuple(position)
	if tup in grid:
		grid[tup]["direction"] += direction
		grid[tup]["steps"] += step
	else:
		grid[tup] = {"direction" : direction, "steps" : step}
	return grid

# grid
g = dict()
g = runWire(g, w1, "1")
g = runWire(g, w2, "2")
direc = str()
#print(g)
closestDistance = sys.maxsize
closestDistancePoint = str()
minSteps = sys.maxsize
minStepsPoint = str()
for key, value in g.items():
	direc = value["direction"]
	if len(direc) > 2:
		if ('R' in direc or 'L' in direc) and ('U' in direc or 'D' in direc) and ('1' in direc and '2' in direc):
			#print("Key {}, direc {}, distance {}".format(key, direc, abs(key[0]) + abs(key[1])))
			d = abs(key[0]) + abs(key[1])
			if d < closestDistance:
				closestDistance = d
				closestDistancePoint = str(key)
			if value["steps"] < minSteps:
				minSteps = value["steps"]
				minStepsPoint = str(key)
		#else:
			#print("Warning: Key {}, direc {}".format(key, value))

print("Closest distance {} with point {} ".format(closestDistance, closestDistancePoint))
print("Min steps {} with point {} ".format(minSteps, minStepsPoint))