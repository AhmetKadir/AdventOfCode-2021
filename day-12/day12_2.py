_inputs = "input12.txt"
_test= "T_inputs_12.txt"
start = -1
pathCount = 0


class Cave:
	def __init__(self, name, index):
		self.name = name
		self.index = index
		self.neighbors = set()
		self.isSmall = self.name.islower()
	
	def addNeighbor(self, neighbor):
		self.neighbors.add(neighbor)


def newCave(caveName):
	global start
	for i in range(0, len(caves)):
		if caveName == caves[i].name:
			if(start == -1 and caves[i].name == "start"):
				start = i
			return i
	
	return -1

def findPaths(theCave, visitSmalls, str):
	str += theCave.name + " + "
	if(theCave.name == "end"):
		global pathCount
		pathCount += 1
		#print(str , "\n")

		return

	if(theCave.isSmall):
		visitCount[theCave.index] += 1
		if visitCount[theCave.index] == 2:
			visitSmalls = False

	for x in theCave.neighbors:
		if((visitCount[x.index] == 1 and visitSmalls) or visitCount[x.index] < 1):
			findPaths(x, visitSmalls, str)
			if(x.name == "end"):
				str += "\n"
	
	visitCount[theCave.index] -= 1
	

caves = []
bigCave = False
nextIndex = 0

with open(_inputs, "r") as f:
	data = f.readline()

	while data:
		data = data.split("-")
		cave1 = data[0]
		cave2 = data[1].strip("\n")

		index1 = newCave(cave1)
		index2 = newCave(cave2)

		if(index1 == -1):
			caveA = Cave(cave1, nextIndex)
			caves.append(caveA)
			index1 = nextIndex
			nextIndex += 1
		
		if(index2 == -1):
			caveB = Cave(cave2, nextIndex)
			caves.append(caveB)		
			index2 = nextIndex	
			nextIndex += 1

		caves[index1].addNeighbor(caves[index2])
		caves[index2].addNeighbor(caves[index1])

		data= f.readline()

isVisited = []
for i in range(0, len(caves)):
	isVisited.append(False)

visitCount = []
for i in range(0, len(caves)):
	visitCount.append(0)

visitCount[start] = 2

findPaths(caves[start], True ," ")

print("Number of total paths =", pathCount )
