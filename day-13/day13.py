_inputs = "input13.txt"
_test= "t_input13.txt"

def totalDots(thePaper):
	count = 0
	for i in thePaper:
		for j in i:
			if(j):
				count += 1
	
	return count


def fold(thePaper):
	line = foldY[0]
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
			elif(letter == "x"):
				foldY.append(location)


		data= f.readline()

for i in range(0, maxX + 1):
	paper.append([])
	for j in range(0, maxY + 1):
		paper[i].append(False)

for i in range(0, len(x)):
	paper[x[i]][y[i]] = True

# for i in paper:
# 	for j in i:
# 		if(j):
# 			print("#", end=" ")
# 		else:
# 			print(".", end=" ")
# 	print("\nNEW LINE")

fold(paper)
print()
result = totalDots(paper)

# for i in paper:
# 	for j in i:
# 		if(j):
# 			print("#", end=" ")
# 		else:
# 			print(".", end=" ")
# 	print()
print("Result =" , result)
