f = open(r"C:\Users\ahmet\OneDrive\Masaüstü\Software\Python\AdventOfCode\inputs.txt", "r")
counter = 0
myLine = f.readline()
myLine = int(myLine.strip('\n'))
temp = myLine

myLine = f.readline()

while myLine:
	myLine = int(myLine.strip('\n'))

	if(myLine > temp):
		counter += 1

	temp = myLine

	myLine = f.readline()
	print(myLine)

f.close()

print(counter)
	