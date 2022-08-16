def isFinished(b):
	for i in b:
		_counter = 0
		for j in i:
			if (j == False):
				break
			else:
				_counter += 1
		if (_counter == 5):
			return True
			

	_counter = 0
	for j in range(0, len(b)):
		for i in range(0, len(b[j])):
			# print("i,j =", i,j)
			# print("b[i][j] =", b[i][j])
			if(b[i][j] == True):
				_counter += 1
				# print("Counter =", _counter)
			else:
				_counter = 0
				break
		if (_counter == 5):
			return True
	return False

	
def sumOfUnmarkeds(b, _board):
	_sum = 0
	for i in range(0, len(b)):
		for j in range(0, len(b[i])):
			if(b[i][j] == False):
				_sum += _board[i][j]
	return _sum


BOARD_SIZE = 5

f = open("testInputs4.txt", "r")
myLine = f.readline()
numbers =myLine.split(",")
for i in numbers:
	i = int(i)

boards = [[[ ]]]

index = 0

myLine = f.readline()
while myLine:
	myLine = myLine.split(" ")

	if(len(myLine) >= 2):
		for i in range(0,BOARD_SIZE):

			for j in range(0, len(myLine)):

				try:
					num = int(myLine[j])
					boards[index][i].append(num)
					tryAgain = False
				except:
					1

			myLine = f.readline()
			myLine = myLine.split(" ")

			if(len(myLine) < 2):
				break
			boards[index].append([])
	
		index += 1
		boards.append([[]])

	myLine = f.readline()

f.close()

markedBoard = [[[]]]

for i in range(0, len(boards)):
	markedBoard.append([[]])
	for j in range(0, len(boards[i])):
		markedBoard[i].append([])
		for k in range(0, len(boards[i][j])):
			markedBoard[i][j].append(False)

isOver = False
markedWinnerBoard = boards[0]
winnerBoard = boards[0]
lastNum = 0
isOver = False

for num in numbers:
	num = int(num)
	for i in range(0,len(boards)):
		for j in range(0, len(boards[i])):
			for k in range(0, len(boards[i][j])) :
				if(boards[i][j][k] == num):
					markedBoard[i][j][k] = True
					if (isFinished(markedBoard[i]) == True):
						markedWinnerBoard = markedBoard[i]
						winnerBoard = boards[i]
						lastNum = num
						isOver = True
						break
			
			if(isOver):
				break
		if isOver:
			break
	if isOver:
		break
_sum = sumOfUnmarkeds(markedWinnerBoard, winnerBoard)


# for a in markedBoard:
# 	for b in a:
# 		print(b)
# 	print("\n")


print(_sum)
print(lastNum)
result =  _sum * lastNum

print("RESULT =",result)


