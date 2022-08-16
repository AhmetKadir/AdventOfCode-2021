N = 1000
_file = "inputs_5.txt"

def mark(x1, y1, x2, y2):
	if(x1 == x2 and y1 != y2):
		if(y1 < y2):
			for i in range(y1, y2 + 1 ):
				coordinates[x1][i] += 1
		else:
			for i in range(y2, y1 + 1):
				coordinates[x1][i] += 1

	elif(y1 == y2 and x1 != x2):
		if(x1 < x2):
			for i in range(x1, x2 + 1):
				coordinates[i][y1] += 1
		else:
			for i in range(x2, x1 + 1):
				coordinates[i][y1] += 1 

	elif(x1+y1 == x2+y2):
		inc = 1 if x1<x2 else -1
		j = y1
		for i in range(x1, x2 + inc, inc):
			coordinates[i][j] += 1
			j += -inc

		
		#x1 = 2 , y1 = 6, x2 = 4 , y2 = 8
	elif(x1-x2 == y1-y2):
		inc = 1
		if( y1 < y2):
			j = y1
			i = x1
		else:
			i = x2
			j = y2
			inc = -1

		for _ in range(x1, x2 + inc, inc):
			coordinates[i][j] += 1
			i += 1
			j += 1
			

f = open(_file, "r")
data = f.readline()

coordinates = [[0] * N for i in range(N)] 	# N*N List

while(data):
	data = data.split("->")
	left = data[0].split(",")
	right = data[1].split(",")
	x1 = int(left[0])
	y1 = int(left[1])
	x2 = int(right[0])
	y2 = int(right[1])

	mark(x1, y1, x2, y2)
	
	data = f.readline()

f.close()

counter = 0
for i in coordinates:
	for val in i:
		if val > 1:
			counter += 1
print()
print("Result =", counter)