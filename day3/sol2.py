def main():
	val = 0
	with open("input.txt","r") as fp:
		currIndex = 0
		ryggsäcks = [0,0,0]
		for line in fp:
			print(line)
			line=line.strip('\n')
			line=list(line)
			ryggsäcks[currIndex] = line
			currIndex = (currIndex +1)%3
			if currIndex == 0:
				val += compareLists(ryggsäcks[0],ryggsäcks[1],ryggsäcks[2])

	print(val)


def compareLists(list1,list2,list3):
	#scoreList=[]
	for i in range(len(list1)):
		for j in range(len(list2)):
			for k in range(len(list3)):
				if list1[i] == list2[j]==list3[k]:
					print(list1[i])
					if(list1[i].islower()):
						return  ((ord(list1[i])-96))
					else:
						return ((ord(list1[i])-64) + 26)



if __name__ == "__main__":
	main()