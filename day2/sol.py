opp = {
	"A" : 1, # Rock
	"B" : 2, # Paper
	"C" : 3 # Scissors
}
you = {
	"X" : 1, # Rock
	"Y": 2, # Paper
	"Z": 3 # Scissors
}

score = 0

with open("question.txt","r") as fp:
	for line in fp:
		l = line.split()
		y=l[1]
		o=l[0]
		youScore = (you[y]-1)%4
		if youScore == 0:
			youScore = 3
		if youScore == opp[o]:
			score+=6
		elif you[y] == opp[o]:
			score += 3
		score += you[y]
print(score)