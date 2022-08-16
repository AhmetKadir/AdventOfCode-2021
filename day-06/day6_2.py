_inputs = "inputs_6.txt"
_test = "T_inputs_6.txt"

########################################

f = open(_inputs, "r")
data = f.read(-1)
f.close()

data = data.split(",")

count = [0] * 9
_temp = [0] * 9

for i in data:
	a = int(i)
	count[a] += 1
	_temp[a] += 1

days = 256
leng = len(count)
for day in range(0, days):
	for i in range(leng - 1, -1, -1):
		if(i == 8):
			count[i] = _temp[0]
		else:
			count[i] = _temp[i+1]
		if(i == 6):
			count[i] += _temp[0]
	for i in range(0, len(_temp)):
		_temp[i] = count[i]

total = 0
for i in count:
	total += i

print("\nAnswer is =", total)
