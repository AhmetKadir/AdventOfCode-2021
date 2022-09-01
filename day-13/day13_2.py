_inputs = "input13.txt"
_test= "t_input13.txt"

def fold_X(thePaper, ind):
	line = foldX[ind]
	for i in range(line + 1, len(thePaper)):
		for j in range(0, len(paper[i])):
			if(thePaper[i][j]):
				_x = 2*line - i

				thePaper[_x][j] = True
	
	for i in range(len(thePaper) -1 , line -1, -1):
		del thePaper[i]


def fold_Y(thePaper, ind):
	line = foldY[ind]
	for i in range(0, len(thePaper)):
		for j in range(line+1, len(thePaper[i])):
			if(thePaper[i][j]):
				_y = 2*line - j

				thePaper[i][_y] = True

	for i in range(len(thePaper) -1 , -1, -1):
		for j in range(len(thePaper[i]) - 1, line-1, -1 ):
			del thePaper[i][j]

paper = []
x= []
y= []
maxX = 0
maxY = 0
foldX = []
foldY = []
nextFoldX = []

with open(_inputs, "r") as f:
	data = f.readline()

	while data:
		if(data[0] != "f" and data[0] != "\n"):

			data = data.split(",")
			val_y = int(data[0])
			val_x = int(data[1])
			y.append(val_y)
			x.append(val_x)

			if(val_x > maxX): maxX = val_x
			if(val_y > maxY): maxY = val_y		

		elif(data[0] == "f"):
			data = data.strip("\n")
			data = data.split(" ")
			letter = data[2][0]

			data = data[2].split("=")
			location = int(data[1])

			if(letter == "y"):
				foldX.append(location)
				nextFoldX.append(True)
			elif(letter == "x"):
				foldY.append(location)
				nextFoldX.append(False)


		data= f.readline()

for i in range(0, maxX + 1):
	paper.append([])
	for j in range(0, maxY + 1):
		paper[i].append(False)

for i in range(0, len(x)):
	paper[x[i]][y[i]] = True

foldXIndex = 0
foldYIndex = 0

for i in range(0, len(nextFoldX)):
	if(nextFoldX[i]):
		fold_X(paper, foldXIndex)
		foldXIndex += 1

	else:
		fold_Y(paper, foldYIndex)
		foldYIndex += 1

print()

for i in paper:
	for j in i:
		if(j):
			print("# ", end="")
		else:
			print("  ", end="")
	print()
# print("Result =" , result)
