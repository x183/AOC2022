

def main():
	val = 0
	with open("input.txt","r") as fp:
		for line in fp:
			print(line)
			line=line.strip('\n')
			line=list(line)
			linelength = int(len(line))
			compartment1 = line[0:int(linelength/2)]
			compartment2 = line[int(linelength/2):linelength]
			res= compareLists(compartment1,compartment2)
			if res!=None:
				val+=res
			print(compartment1)
			print(compartment2)
	print(val)


def compareLists(list1,list2):
	#scoreList=[]
	for i in range(len(list1)):
		for j in range(len(list2)):
			if list1[i] == list2[j]:
				print(list1[i])
				if(list1[i].islower()):
					return  ((ord(list1[i])-96))
				else:
					return ((ord(list1[i])-64) + 26)



if __name__ == "__main__":
	main()