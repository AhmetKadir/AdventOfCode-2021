_inputs = "input14.txt"
_test= "sample14.txt"

def insertionRules(rule):
	theKey = rule[0] + rule[1]
	value = pairs.get(theKey)
	if(value is not None and value != 0):
		temp.append(rule[0] + rule[6])
		temp.append(rule[6] + rule[1])
		tempVal.append(value)
		tempVal.append(value)

def insert():
	for i in range(0, len(temp)):
		if(i % 2 == 0):
			theKey = temp[i][0] + temp[i+1][1]
			value = pairs.get(theKey)
			pairs.update({theKey: value - tempVal[i]})

		theKey = temp[i]
		value = pairs.get(theKey)
		if (value is not None):
			pairs.update({theKey: (value + tempVal[i])})
		else :
			pairs.setdefault(theKey, tempVal[i])
		
rules = []
pairs = {}

with open(_inputs, "r") as f:
	data = f.readline()
	template = list(data.strip("\n"))

	data = f.readline()

	while data:
		data = data.strip("\n")
		if (len(data) > 1):
			rules.append(data)

		data = f.readline()


for i in range(0, len(template) - 1):
	theKey = template[i] + template[i+1]
	pairs.setdefault(theKey, 1)

temp = []
tempVal = []
steps = 0

while (steps < 40):
	for rule in rules:
		insertionRules(rule)

	insert()
	temp.clear()
	tempVal.clear()

	steps += 1


count = []
for i in range(0,28):
	count.append(0)

pairList = list(pairs.items())

for i in pairList:
	count[ord(i[0][0]) - ord("A")] += i[1]

# for the last element of the template
lastEl = ord(template[len(template) - 1])
count[lastEl - ord("A")] += 1 

max = count[ord(template[0]) - ord("A")]
min = count[ord(template[0]) - ord("A")]

for i in count :
	if(i == 0):
		continue

	if i > max:
		max = i
	elif i < min:
		min = i

result = max - min
print("\nresult =", result)

