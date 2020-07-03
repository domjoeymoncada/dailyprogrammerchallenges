from random import randrange

def roll_dice() -> list:
  # Returns a list of random numbers 
  dice = [randrange(1,7) for i in range(0,6)]
  return dice

def yahtzee_upper(dice: list) -> int:
  # Returns an integer that is the upper section of the Yahtzee
  result = [roll_score(i, dice) for i in range(1, 7)]
  return get_highest_score(result)

def roll_score(index: int, dice: list) -> int:
  # Returns an integer that is the number of occurrence x index
  occurrences = 0

  for i in range(0, len(dice)):
    if dice[i] == index:
      occurrences  += 1
  
  return index * occurrences

def get_highest_score(result: list) -> int:
  # Returns an integer that is the highest among the scores
  highest = 0

  for i in range(0, len(result)):
    if result[i] > highest:
      highest = result[i]
  
  return highest

roll = roll_dice()
score = yahtzee_upper(roll)
print(score)