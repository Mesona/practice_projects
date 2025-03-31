import sys

print("Welcome to Rock Paper Scissors!")
gameContinue = True

while gameContinue == True:
  player1 = input("Player 1, which do you choose: R/P/S? ")
  player2 = input("Player 2, which do you choose: R/P/S? ")
  if player1.lower() == "r":
    if player2.lower() == "s":
      print("Player 1 wins!")
    elif player2.lower() == "p":
      print("Player 2 wins!")
    elif player2.lower() == "r":
      print("The game is a draw!")
  elif player1.lower() == "p":
      if player2.lower() == "r":
        print("Player 1 wins!")
      elif player2.lower() == "s":
        print("Player 2 wins!")
      elif player2.lower() == "p":
        print("The game is a draw!")
  elif player1.lower() == "s":
      if player2.lower() == "p":
        print("Player 1 wins!")
      elif player2.lower() == "r":
        print("Player 2 wins!")
      elif player2.lower() == "s":
        print("The game is a draw!")
  else:
    print("Invalid input detected! Please enter only 'P' or 'R' or 'S' ")

  next = input("Would you like to play again? Y/N ")
  if next.lower() == "y":
    continue
  else:
    gameContinue = False

print("Thanks for playing!")

