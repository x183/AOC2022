
def findMax(arr):
	max = arr[0]
	high = 0
	for i in range(1, len(arr)):
		if arr[i] > max:
			max = arr[i]
			high = i
	return max

elfList=[]
totalAmount=0
sCount=0
f = open("quest.txt", "r")
for inp in f:
	if inp =='\n':
		elfList.append(totalAmount)
		totalAmount = 0
		sCount+=1
	else:
		totalAmount += int(inp)
highScore=[]
for i in range(3):
	highScore.append(findMax(elfList))
	elfList.remove(highScore[i])
result=0
for x in highScore:
	result += x
print(result)
