import random
from random import randint
#board = "  A B C \n" +"1|X|X|X|\n" +"2|X|X|X|\n" +"3|X|X|X|\n"
board = {
	"A" : [ " ", " ", " "],
	"B" : [ " ", " ", " "],
	"C" : [ " ", " ", " "],
}
def putXOrO(location, xOrO, board):
	#if location in board is unoccupied, replace with xOrO
	row = location[0]
	column = int(location[1])
	if ( board[row][column-1] == " "):
		board[row][column-1] = xOrO
		return True
		
	
def drawBoard(board):
	strBoard = "  1 2 3 \n" + "A"
	for i in range(len(board["A"])):
		strBoard += "|" + board["A"][i]
	strBoard += "|\nB"
	for j in range(len(board["B"])):
		strBoard += "|" + board["B"][j]
	strBoard += "|\nC"
	for x in range(len(board["C"])):
		strBoard += "|" + board["C"][x]
	strBoard += "|"
	
	print(strBoard)

def seeIfWon(board):
	#top row
	if(board["A"][0] == board["A"][1] == board["A"][2] and board["A"][0] != " "):
		if(board["A"][0] == "X"):
			print("X has won!")
		else:
			print("O has won!")
		return True
	#middle row
	elif(board["B"][0] == board["B"][1] == board["B"][2] and board["B"][0] != " "):
		if(board["B"][0] == "X"):
			print("X has won!")
		else:
			print("O has won!")
		return True
	#bottom row
	elif(board["C"][0] == board["C"][1] == board["C"][2] and board["C"][0] != " "):
		if(board["C"][0] == "X"):
			print("X has won!")
		else:
			print("O has won!")
		return True
	#diagonal topLeft to bottomRight
	elif(board["A"][0] == board["B"][1] == board["C"][2] and board["A"][0] != " "):
		if(board["A"][0] == "X"):
			print("X has won!")
		else:
			print("O has won!")
		return True
	#diagonal bottomLeft to topRight
	elif(board["A"][2] == board["B"][1] == board["C"][0] and board["A"][2] != " "):
		if(board["A"][2] == "X"):
			print("X has won!")
		else:
			print("O has won!")
		return True
	#1st column
	elif(board["A"][0] == board["B"][0] == board["C"][0] and board["A"][0] != " "):
		if(board["A"][0] == "X"):
			print("X has won!")
		else:
			print("O has won!")
		return True
	#2nd column
	elif(board["A"][1] == board["B"][1] == board["C"][1] and board["A"][1] != " "):
		if(board["A"][1] == "X"):
			print("X has won!")
		else:
			print("O has won!")
		return True
	#3rd column
	elif(board["A"][2] == board["B"][2] == board["C"][2] and board["A"][2] != " "):
		if(board["A"][2] == "X"):
			print("X has won!")
		else:
			print("O has won!")
		return True
	else:
		return False;
			
def cpuPlay( xOrO, board):
	possiblePos = []
	for i in range(len(board["A"])):
		if board["A"][i] == " ":
			possiblePos.append("A" + str(i+1))
	for i in range(len(board["B"])):
		if board["B"][i] == " ":
			possiblePos.append("B" + str(i+1))
	for i in range(len(board["C"])):
		if board["C"][i] == " ":
			possiblePos.append("C" + str(i+1))
	
	if(len(possiblePos)>1):
		rPos = randint(0, len(possiblePos)-1)
		putXOrO( possiblePos[rPos], xOrO, board)
	else:
		putXOrO(possiblePos[0],xOrO, board)

def resetBoard(board):
	board["A"] = [" ", " ", " "]
	board["B"] = [" ", " ", " "]
	board["C"] = [" ", " ", " "]

def playGame(startingPlayer, board):
	i = 0
	if startingPlayer == "me" or startingPlayer == "player":
		while i < 9:
			if i == 0:
				drawBoard(board)
			xPos = input("Enter position for X")
			enteredCorrectly = putXOrO(xPos, "X", board)
			while not enteredCorrectly:
				xPos = input("Enter different position for X")
				enteredCorrectly = putXOrO(xPos, "X", board)
			i+=1
			drawBoard(board)
			if seeIfWon(board):
				break
			print("CPU's Turn")
			cpuPlay("O", board)
			i+=1
			drawBoard(board)
			if seeIfWon(board):
				break
	else:
		while i < 9:
			print("CPU's Turn")
			cpuPlay("X", board)
			i+=1
			drawBoard(board)
			if seeIfWon(board):
				break
			oPos = input("Enter Position for O")
			enteredCorrectly = putXOrO(oPos, "O", board)
			while not enteredCorrectly:
				xPos = input("Enter different position for X")
				enteredCorrectly = putXOrO(xPos, "X", board)
			i+=1
			drawBoard(board)
			if seeIfWon(board):
				break
	if(not seeIfWon(board)):
		print("It's a draw")
	

playAgain = True
while playAgain:
	resetBoard(board)
	startingPlayer = input("Do you want CPU or player to start?")
	playGame(startingPlayer, board)
	answer = input("Do you want to play again?")
	if answer == "yes":
		playAgain = True
	else:
		playAgain = False
	