f = open(r"C:\Users\ahmet\OneDrive\Masaüstü\Software\Python\AdventOfCode\inputs_3.txt", "r")

myLine = f.readline()
myLine = myLine.strip("\n")

_zeros = 0
_ones = 0

if(myLine[0] == "0"):
	_zeros += 1
elif(myLine[0] == "1"):
	_ones += 1

lenBits = len(myLine)			

oxyList = []
co2List = []

while myLine:
	myLine = myLine.strip("\n")
	oxyList.append(myLine)
	co2List.append(myLine)
	if(myLine[0] == "0"):
		_zeros += 1
	elif(myLine[0] == "1"):
		_ones += 1

	myLine = f.readline()

f.close()

# oxygen calculation

moreOnes = False
index = 0
tempList = []
tempOnes = _ones
tempZeros = _zeros

while(_ones + _zeros > 1):
	print("ONES AND ZEROS :" , _ones, _zeros)
	if (_ones >= _zeros):
		moreOnes = True
	else:
		moreOnes = False
		
	if(moreOnes):
		for i in oxyList:
			if (i[index] == "1"):
				tempList.append(i)
	else:
		for i in oxyList:
			if (i[index] == "0"):
				tempList.append(i)

	oxyList.clear()
	for i in tempList:
		oxyList.append(i)
	tempList.clear()			

	index +=1 
	if(index >= lenBits):
		break

	_ones = 0
	_zeros = 0

	for i in oxyList:
		if(i[index] == "0"):
			_zeros += 1
		elif(i[index] == "1"):
			_ones += 1

oxyResult = 0

_power = 0
for j in reversed(range(0,lenBits)):
	if(oxyList[0][j] == "1"):
		oxyResult += 2**_power
	_power += 1

# CO2 Calculation

moreOnes = False
index = 0
tempList = []
_zeros = tempZeros
_ones = tempOnes

while(_ones + _zeros > 1):
	print("ONES AND ZEROS :" , _ones, _zeros)
	if (_ones >= _zeros):
		moreOnes = True
	else:
		moreOnes = False
		
	if(moreOnes):
		for i in co2List:
			if (i[index] == "0"):
				tempList.append(i)
	else:
		for i in co2List:
			if (i[index] == "1"):
				tempList.append(i)

	co2List.clear()
	for i in tempList:
		co2List.append(i)
	tempList.clear()			

	index +=1 
	if(index >= lenBits):
		break

	_ones = 0
	_zeros = 0

	for i in co2List:
		if(i[index] == "0"):
			_zeros += 1
		elif(i[index] == "1"):
			_ones += 1

co2Result = 0

_power = 0
for j in reversed(range(0,lenBits)):
	if(co2List[0][j] == "1"):
		co2Result += 2**_power
	_power += 1

print(oxyList)
print(co2List)
print(oxyResult)
print(co2Result)
print(oxyResult * co2Result)
	
