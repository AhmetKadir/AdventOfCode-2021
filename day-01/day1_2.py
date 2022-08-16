f = open("inputs.txt", "r")
counter = 0
myLine = f.readline()
num1 = int(myLine.strip('\n'))

myLine = f.readline()
num2 = int(myLine.strip('\n'))

temp = 100000

while myLine:
	myLine = f.readline()
	if(len(myLine) < 1):
		break
	
	num3 = int(myLine.strip('\n'))

	sum = num1 + num2 + num3

	if(sum > temp):
		counter += 1

	num1 = num2
	num2 = num3
	temp = sum

f.close()
print("Result:", counter)