_inputs = "inputs_8.txt"
_test= "T_inputs_8.txt"

			#   a  b  c  d  e  f  g
#OccurenceAr = [8, 6, 8, 7, 4, 9, 7]

arr = [42, 17, 34, 39, 30, 37, 41, 25, 49, 45]

def decode(sign, _countOccurence):
	total = 0
	for i in range(0, len(sign)):
		if(sign[i] == "a"):
			myNum = _countOccurence[0]
		elif(sign[i] == "b"):
			myNum = _countOccurence[1]
		elif(sign[i] == "c"):
			myNum = _countOccurence[2]
		elif(sign[i] == "d"):
			myNum = _countOccurence[3]
		elif(sign[i] == "e"):
			myNum = _countOccurence[4]
		elif(sign[i] == "f"):
			myNum = _countOccurence[5]
		elif(sign[i] == "g"):
			myNum = _countOccurence[6]
			
		total += myNum
	
	return findTheNum(total)

def findTheNum(total):
	for i in range(0, len(arr)) :
		if (total == arr[i]):
			return i
	return 0


# can identify 1 4 7 8

result = 0
f = open(_inputs, "r")
data = f.readline()

while data:
	countOccurence =[0, 0, 0, 0, 0, 0, 0]
	number = ""
	data = data.split("|")
	first = data[0].split(" ")
	second = data[1].split(" ");

	#print(second)
	for signal in first:
		if(len(signal) > 1):
			for i in  range(0, len(signal)):
				if(signal[i] == "a"):
					countOccurence[0] += 1
				elif(signal[i] == "b"):
					countOccurence[1] += 1
				elif(signal[i] == "c"):
					countOccurence[2] += 1
				elif(signal[i] == "d"):
					countOccurence[3] += 1
				elif(signal[i] == "e"):
					countOccurence[4] += 1
				elif(signal[i] == "f"):
					countOccurence[5] += 1
				elif(signal[i] == "g"):
					countOccurence[6] += 1

	for signal in second:
		#print(signal)
		if(len(signal) > 1):
			signal = signal.strip("\n")
			temp = str(decode(signal, countOccurence))
			number += temp
	number = int(number)
	result += number

	data = f.readline()
	
f.close()

print(result)