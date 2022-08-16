_inputs = "inputs_9.txt"
_test= "T_inputs_9.txt"

arr = []
alreadyVisited = []
sizes = [0, 0, 0]
sizeCount = 0

def findSize(x, y, heightMap):
	if(heightMap[x][y] == 9):
		return 

	if(alreadyVisited[x][y] == True):
		return

	alreadyVisited[x][y] = True
		
	# go left	
	if(y-1 >= 0 ):
		findSize(x, y-1, heightMap)
	# go right
	if(y+1 < len(heightMap[x])):
		findSize(x, y+1, heightMap)
	# go up
	if(x-1 >= 0 ):
		findSize(x-1, y, heightMap)
	# go down
	if(x+1 < len(heightMap)):
		findSize(x+1, y, heightMap)

	global sizeCount
	sizeCount += 1



f = open(_inputs, "r")
data = f.readline()
index = 0

while data:
	data = data.strip("\n")
	arr.append([])
	alreadyVisited.append([])
	for i in range(0, len(data)):
		arr[index].append(int(data[i]))
		alreadyVisited[index].append(False)
	index += 1

	data = f.readline()
f.close()

for i in range(0, len(arr)):
	for j in range(0, len(arr[i])):
		sizeCount = 0
		if(alreadyVisited[i][j]):
			continue
		findSize(i, j, arr)
		sizes.sort()
		if (sizeCount > sizes[0]):
			sizes[0] = sizeCount


result = 1		

for x in sizes:
	print(x)
	result *= x

print("\nResult = ", result)

