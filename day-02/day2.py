horizontal = 0
depth = 0

f = open(r"C:\Users\ahmet\OneDrive\Masaüstü\Software\Python\AdventOfCode\inputs_2.txt", "r")
myLine = f.readline()
myLine = myLine.split(" ")

while(myLine):
	val = int(myLine[1])
	if(myLine[0] == "forward"):
		horizontal += val
	elif(myLine[0] == "up"):
		depth -= val
	elif(myLine[0] == "down"):
		depth += val
	else:
		break

	myLine = f.readline()
	myLine = myLine.split(" ")
	print(myLine)
	if(len(myLine) != 2):
		break

f.close()

print(horizontal * depth)