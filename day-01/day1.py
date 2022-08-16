f = open("inputs.txt", "r")
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

f.close()

print("Result:", counter)
	