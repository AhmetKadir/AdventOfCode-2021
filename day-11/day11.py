_inputs = "input11.txt"
_test= "T_inputs_11.txt"

def increase(x, y):
	if(flashed[x][y]):
		return
	
	if(arr[x][y] != 9):
		arr[x][y] += 1
				
	elif(arr[x][y] == 9):
		arr[x][y] = 0
		flashed[x][y] = True
		global flashCount
		flashCount += 1

		if(x-1 >= 0):
			increase(x-1, y)
			if(y-1 >= 0):
				increase(x-1, y-1)
			if(y+1 < len(arr)):
				increase(x-1, y+1)
		if(x+1 < len(arr)):
			increase(x+1, y)
			if(y-1 >= 0):
				increase(x+1, y-1)
			if(y+1 < len(arr)):
				increase(x+1, y+1)
		if(y-1 >= 0):
			increase(x, y-1)
		if(y+1 < len(arr)):
			increase(x, y+1)

def refreshFlashed():
	for i in range(0, len(arr)):
		for j in range(0, len(arr[i])):
			flashed[i][j] = False

def allFlashed():
	for a in flashed:
		for b in a:
			if (not b):
				return False
	return True

ind = 0
arr = []
f = open(_inputs, "r")
data = f.readline()

while data:
	data = data.strip("\n")
	arr.append([])
	for i in range(0, len(data)):
		arr[ind].append(int(data[i]))
	
	data = f.readline()
	ind += 1

f.close()

steps = 0
flashCount = 0
flashed = []
for i in range(0, len(arr)):
		flashed.append([])
		for j in range(0, len(arr[i])):
			flashed[i].append(False)

while (1):
	refreshFlashed()
	
	for i in range(0, len(arr)):
		for j in range(0, len(arr[i])):
				increase(i, j)

	steps += 1

	if(allFlashed()):
		print("Step =", steps)
		break

print("Total Flashes =", flashCount)
