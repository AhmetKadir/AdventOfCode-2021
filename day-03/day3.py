zeros = []
ones = []
lenBits = 0

f = open("inputs_3.txt", "r")
myLine = f.readline()

while myLine:

	if((lenBits) == 0):
		lenBits = len(myLine)	
	
	index = 0

	for bit in myLine:
		if(bit == "0"):
			if(len(zeros) <= index):
				zeros.append(1)
				ones.append(0)
			else:
				zeros[index] += 1
		elif(bit == "1"):
			if(len(ones) <= index):
				ones.append(1)
				zeros.append(0)
			else:
				ones[index] += 1
		index += 1

	myLine = f.readline()

f.close()

gama = []
epsilon = []

for i in range(0, lenBits - 1):
	if zeros[i] > ones[i]:
		gama.append(0)
		epsilon.append(1)
	else:
		gama.append(1)
		epsilon.append(0)

dec_gama = 0
dec_epsilon = 0

print(gama)
print(epsilon)

bin_index = len(gama) - 1
for j in range( 0, len(gama)):
	if(gama[bin_index] == 1):
		dec_gama += 2**j
	if(epsilon[bin_index] == 1):
		dec_epsilon += 2**j

	bin_index -= 1

print(dec_gama)
print(dec_epsilon)

print("Result =", dec_epsilon * dec_gama)

