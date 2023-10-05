"""Import logos and randint function from replit.Randint help our code to choose random number between 1-100. """
from art import logo
from random import randint
from win import win_logo

EASY_LEVEL_LIVES=10
HARD_LEVEL_LIVES=5
lives=0
def check_answer(guess,lives,answer):
  """Check answer function determines whether our guess is low or high from the answer. """
  if answer<guess:
    print("Too high guess, repeat again!!!")
    """We use return instead of global variable beacause is it more easy and more understandable for other developers.We lower the lives of player. """
    return lives-1
  elif answer>guess:
    print("Too low guess, repeat again!!")
    return lives -1
  else:
    print("You are unbeatable.Right number!!!")
    print(win_logo)

def lives_level():
  """This function give a chance to player to choose easy or hard level."""
  lives=input("Please enter your level-Choose 'easy' for 10 lives and 'hard' for 5 lives?")
  if lives=='easy':
    return EASY_LEVEL_LIVES
  else:
    return HARD_LEVEL_LIVES

def guess_game():
  print(logo)
  print("Welcome to the NUMBER GUEASSING GAME.")
  print("We believe you can do it.I am thinking for a number.= between 1-100.")
  """With randint computer picks number. """
  answer =randint(1,100)
  """Call lives level function."""
  lives=lives_level()

  guess=0
  """Use a while loop so that the game can be repeated until the player lives end or the player guess right number."""
  while guess!=answer:
    print(f"You have {lives} lives remaining.")
    guess=int(input("Please make a guess:"))
    """Call the check answer function."""
    lives=check_answer(guess, lives, answer)
    if lives == 0:
      print("Sorry but you lose the game out of lives!")
      """We use return to end the game and end the while loop."""
      return
    elif guess !=answer:
      print("Guess again!!!")



guess_game()
      
  