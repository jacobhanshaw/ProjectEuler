from random import randrange

NUM_TOP_ELEMENTS = 3

BOARD_SIZE = 40

NUM_CARDS = 16
SIDES_OF_DICE = 4
NUM_DICE_ROLLS = 10**6

doubles = 0
position = 0
chanceIndex = 0
comChestIndex = 0
board = [0] * BOARD_SIZE

def chance():
  global position, chanceIndex
  chanceDest = [ 0, 10, 11, 24, 39, 5 ]
  chanceIndex = (chanceIndex + 1) % 16

  if chanceIndex < 6:
    position = chanceDest[chanceIndex]
  elif chanceIndex < 8:
    if (position == 7):
			position = 15
    elif (position == 22):
			position = 25
    else:
			position = 5
  elif chanceIndex == 8:
		position = 28 if position == 22 else  12
  elif chanceIndex == 9:
    position -= 3

def community_chest():
  global position, comChestIndex
  comChesDest = [ 0, 10]
  comChestIndex = (comChestIndex + 1) % 16

  if comChestIndex < 2:
    position = comChesDest[comChestIndex]


for i in range(NUM_DICE_ROLLS):
  rollA = randrange(SIDES_OF_DICE) + 1
  rollB = randrange(SIDES_OF_DICE) + 1

  if rollA == rollB:
    doubles += 1
  else:
    doubles = 0

  if(doubles > 2):
    doubles = 0
    position = 10
  else:
    position = (position + rollA + rollB) % BOARD_SIZE
 
    # Chance first as chance can go to community chest
    if (position == 7 or position == 22 or position == 36):
      chance()
    
    if (position == 2 or position == 17 or position == 33):
      community_chest()

    if (position == 30):
      position = 10

  board[position] += 1

result = ""
topSquares = sorted(range(len(board)), key=lambda x: board[x], reverse=True)[:NUM_TOP_ELEMENTS]
for square in topSquares:
  if(square < 10):
    result += "0"
  result += str(square)

print result
