opp = {
	"A" : 1, # Rock
	"B" : 2, # Paper
	"C" : 3 # Scissors
}
you = {
	"X" : 1, # Lose
	"Y": 2, # Draw
	"Z": 3 # Win
}
invOpp ={
	1 : "A",
	2 : "B",
	3 : "C"
}

score = 0

with open("test.txt","r") as fp:
	for line in fp:
		l = line.split()
		y=l[1]
		o=l[0]
		if (y== "X"):
			youScore = (opp[o]-1)%4
			if youScore == 0:
				youScore = 3
			y=invOpp[youScore]
		elif y=="Y":
			youScore = opp[o]
			y=invOpp[youScore]
		else:
			youScore = (opp[o]-2)%4
			if youScore == 0:
				youScore = 3
			y=invOpp[youScore]
		print(f"you: %s\n\topponent: %s",youScore,opp[o])
		if youScore == opp[o]:
			score+=3
			print("draw")
		elif you[y] == opp[o]:
			print("draw")
			score += 3
		score += youScore
print(score)