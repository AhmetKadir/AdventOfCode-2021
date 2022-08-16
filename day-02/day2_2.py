horizontal = 0
depth = 0
aim = 0

f = open(r"C:\Users\ahmet\OneDrive\Masaüstü\Software\Python\AdventOfCode\inputs_2.txt", "r")
myLine = f.readline()
myLine = myLine.split(" ")

while(myLine):
	val = int(myLine[1])
	dir = myLine[0]

	if(dir == "forward"):
		horizontal += val
		depth += val * aim
	elif(dir == "up"):
		aim -= val
	elif(dir == "down"):
		aim += val
	else:
		break

	myLine = f.readline()
	myLine = myLine.split(" ")
	print(myLine)
	if(len(myLine) != 2):
		break

f.close()

print(horizontal * depth)