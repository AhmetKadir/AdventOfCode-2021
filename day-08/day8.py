_inputs = "inputs_8.txt"
_test= "T_inputs_8.txt"

def decode(sign):
	if(len(sign) == 2):
		return True
	elif(len(sign) == 3):
		return True
	elif(len(sign) == 4):
		return True
	elif(len(sign) == 7):
		return True
	else: return False
	

count = 0
f = open(_inputs, "r")
data = f.readline()

while data:
	data = data.split("|")
	second = data[1].split(" ");
	for signal in second:
		signal = signal.strip("\n")
		if(decode(signal)):
			count += 1

	data = f.readline()
	
f.close()

print("\nResult =",count)