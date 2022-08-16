_inputs = "inputs_9.txt"
_test= "T_inputs_9.txt"

arr = []

f = open(_inputs, "r")
data = f.readline()
index = 0

while data:
	data = data.strip("\n")
	arr.append([])
	for i in range(0, len(data)):
		arr[index].append(int(data[i]))
	index += 1

	data = f.readline()

f.close()

min = True
totalRisk = 0

for i in range(0, len(arr)):
	for j in range(0, len(arr[i])):
		min = True
		num = arr[i][j]
		if(j-1 >= 0):
			if(num >= arr[i][j-1]):
				min = False
				continue

		if(j+1 != len(arr[i])):
			if(num >= arr[i][j+1]):
				min = False
				continue

		if(i-1 >= 0):
			if(num >= arr[i-1][j]):
				min = False
				continue

		if(i+1 != len(arr)):
			if(num >= arr[i+1][j]):
				min = False
				continue
		
		if (min == True):
			totalRisk += num + 1

print("\nResult =", totalRisk)
