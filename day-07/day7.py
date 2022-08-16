_inputs = "inputs_7.txt"
_test = "T_inputs_7.txt"

f = open(_inputs, "r")
data = f.read(-1)

f.close()

data = data.split(",")

for i in range(0, len(data)):
	data[i] = int(data[i])

min = 1

for i in data:
	if(i != 0):
		min *= i
total = 0

for i in range(0, len(data)):
	total = 0
	for j in data:
		dist = i-j
		if(dist <= 0):
			dist *= -1
		
		total += (dist*(dist+1) / 2)

	if total < min:
		min = total

print ("\nResult =", min)