global finishedCounter
NUMBER_OF_BOARDS = 100

def isFinished(b):
	for i in range(0, len(b)):
		_counter = 0
		for j in range(0, len(b[i])):
			# print(i,j)
			# print(b[i][j])
			if (b[i][j] == False):
				break
			else:
				_counter += 1
				# print("i,j", i, j)
				# print("counter =", _counter)
		if (_counter == 5):
			# print("----------------------FINISHED------------------")

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
			# print("----------------------FINISHED------------------")
			return True
	return False

	
def sumOfUnmarkeds(b, _board):
	_sum = 0
	for i in range(0, len(b)):
		for j in range(0, len(b[i])):
			if(b[i][j] == False):
				_sum += _board[i][j]
	return _sum

def oneLastBoard(markedBoards, boards):
	for i in range(0, len(boards)):
		global finishedCounter
		if(finishedBoards[i] == False):
			# print(i, ". board ------------------------>")
			if(isFinished(markedBoards[i]) == True):
				finishedCounter += 1
				finishedBoards[i] = True
	
	if (finishedCounter == (len(boards))):
		# print("Finished boards:\n", finishedBoards)
		# print("Finished counter:", finishedCounter)
		return True
	else:
		return False



BOARD_SIZE = 5

f = open("inputs_4.txt", "r")
myLine = f.readline()
numbers =myLine.split(",")


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
				except:
					1

			myLine = f.readline()
			myLine = myLine.split(" ")

			if(len(myLine) < 2):
				break
			boards[index].append([])
	
		index += 1

	myLine = f.readline()

	if (index < NUMBER_OF_BOARDS - 1 ):
		boards.append([[]])


f.close()

markedBoards = [[[]]]

for i in range(0, len(boards)):
	for j in range(0, len(boards[i])):
		for k in range(0, len(boards[i][j])):
			markedBoards[i][j].append(False)
		if (j<len(boards[i]) - 1):
			markedBoards[i].append([])
	if(i < len(boards) - 1):
		markedBoards.append([[]])


isOver = False
markedWinnerBoard = boards[0]
winnerBoard = boards[0]
lastNum = 0
isOver = False

finishedBoards = []

for i in range(0, len(boards)):
	finishedBoards.append(False)
finishedCounter = 0


for num in numbers:
	num = int(num)
	for i in range(0,len(boards)):
		for j in range(0, len(boards[i])):
			if(finishedBoards[i] == True):
				break;
			for k in range(0, len(boards[i][j])) :
				if(boards[i][j][k] == num):
					markedBoards[i][j][k] = True
					# for a in markedBoards:
					# 	for b in a:
					# 		print("->", b)
					# 	print("\n")
					if(oneLastBoard(markedBoards, boards) == True):
						isOver = True
						markedWinnerBoard = markedBoards[i]
						winnerBoard = boards[i]
						lastNum = num			
						break
			if isOver:
				break
		if isOver:
			break
	if isOver:
		break

_sum = sumOfUnmarkeds(markedWinnerBoard, winnerBoard)

# count = 0
# for a in boards:
# 	for b in a:
# 		print("->", b)
# 	print(count)
# 	count += 1

print("marked Winner board is:\n", markedWinnerBoard)
print("Winner board is:\n", winnerBoard)


# for a in markedBoards:
# 	for b in a:
# 		print("->", b)
# 	print("\n")

# for i in range(0, len(boards)):
# 	if(finishedBoards[i] == False):
# 		for j in range(0, len(boards[i])):
# 			for k in range(0, len(boards[i][j])):
# 				print(markedBoards[i][j][k])
# 			print("----")
			


print(_sum)
print(lastNum)
result =  _sum * lastNum

print("RESULT =",result)


