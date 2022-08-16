f = open(r"C:\Users\ahmet\OneDrive\Masaüstü\Software\Python\AdventOfCode\inputs.txt", "r")
counter = 0
myLine = f.readline()
num1 = int(myLine.strip('\n'))

myLine = f.readline()
num2 = int(myLine.strip('\n'))

temp = 100000

while myLine:
	myLine = f.readline()
	num3 = int(myLine.strip('\n'))

	sum = num1 + num2 + num3
	print(sum)
	print(temp)
	if(sum > temp):
		counter += 1

	num1 = num2
	num2 = num3
	temp = sum
	
	if(num3 == 2583):
		break

f.close()
print(counter)