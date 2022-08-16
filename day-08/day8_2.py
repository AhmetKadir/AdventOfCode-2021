_inputs = "inputs_8.txt"
_test= "T_inputs_8.txt"

			#   a  b  c  d  e  f  g
#OccurenceAr = [8, 6, 8, 7, 4, 9, 7]

arr = [42, 17, 34, 39, 30, 37, 41, 25, 49, 45]

def decode(sign, _countOccurence):
	total = 0
	for i in range(0, len(sign)):
		ind = ord(sign[i]) - ord('a')
		myNum = _countOccurence[ind]
	
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

	for signal in first:
		if(len(signal) > 1):
			for i in  range(0, len(signal)):
				num = ord(signal[i]) - ord('a')
				countOccurence[num]+=1

	for signal in second:
		if(len(signal) > 1):
			signal = signal.strip("\n")
			temp = str(decode(signal, countOccurence))
			number += temp
	number = int(number)
	result += number

	data = f.readline()
	
f.close()

print("\nResult =", result)