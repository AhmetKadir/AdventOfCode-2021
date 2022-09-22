_inputs = "input14.txt"
_test= "sample14.txt"

def insertPair(rule):
	lenTemp = len(template) - 1
	i = 0
	while (i < lenTemp):
		if(newPair[i] or newPair[i+1]):
			i += 1
			continue
		
		if(rule[0] == template[i] and rule[1] == template[i+1]):
			template.insert(i+1, rule[6])
			newPair.insert(i+1, True)
			lenTemp += 1
		i += 1
		

rules = []

with open(_inputs, "r") as f:
	data = f.readline()
	template = list(data.strip("\n"))

	data = f.readline()

	while data:
		data = data.strip("\n")
		if (len(data) > 1):
			rules.append(data)

		data = f.readline()

steps = 0
max = 0
min = 0
newPair = []

for i in range(0, len(template)):
	newPair.append(False)

while(steps < 10):
	for rule in rules:
		insertPair(rule)

	for i in range(0, len(newPair)):
		newPair[i] = False
	steps += 1


count = []
for i in range(0,28):
	count.append(0)

for letter in template:
	count[ord(letter) - ord("A")] += 1

max = count[ord(template[0]) - ord("A")]
min = count[ord(template[0]) - ord("A")]

for i in count :
	if(i == 0):
		continue

	if i > max:
		max = i
	elif i < min:
		min = i

print("max =", max)
print("min =", min)
print("result = ", max , " -", min)
print("\nresult =", max - min)

