_inputs = "inputs_6.txt"
_test = "T_inputs_6.txt"

f = open(_inputs, "r")
data = f.read(-1)
data = data.split(",")

for i in range(0, len(data)):
	data[i] = int(data[i])

for i in range(0, 80):
	for j in range(0, len(data)):
		if(data[j] == 0):
			data[j] = 6
			data.append(8)
		else:
			data[j] -= 1

# for i in data:
# 	print (i, ",", end = " ")

print("Answer is:", len(data))