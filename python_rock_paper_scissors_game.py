# Written by Emin Ayyıldız
print("Written by Emin Ayyıldız")

import random

choices = ["rock", "paper", "scissors"]
rock = [0]
paper = [1]
scissors = [2]
print("Welcome to Rock, Paper, Scissors. Press q to end the game")

score_user = 0
score_computer = 0
ties = 0


while True:
  selection = input("Please enter your selection :")
  computer_selection = random.choice(choices)
  if selection == "rock" or selection == "ROCK" or selection == "tas":
    if computer_selection == "rock":
      ties =ties +1
      print("Scoreless","Played",ties,"times")
    elif computer_selection == "paper":
      ties =ties +1
      score_computer +=1
      print("Computer Won ")
      print("Score = ",score_user,score_computer)
    elif computer_selection == "scissors":
      ties =ties +1
      score_user +=1
      print("User won")
      print("Score = ",score_user,score_computer)
  elif selection == "paper" or selection == "PAPER" or selection == "kagıt":
    if computer_selection =="paper":
      ties =ties +1
      print("Scoreless","Played",ties,"times")

    elif computer_selection == "rock":
      ties =ties +1
      score_user +=1
      print("User won")
      print("Score = ",score_user,score_computer)

    elif computer_selection =="scissors":
      ties =ties +1
      score_computer +=1
      print("Computer Won ")
      print("Score = ",score_user,score_computer)
  elif selection == "scissors" or selection == "SCISSORS" or selection == "makas":
    if computer_selection == "scissors":
      ties =ties +1
      print("Scoreless","Played",ties,"times")

    elif computer_selection == "paper":
      ties =ties +1
      score_user +=1
      print("User won")
      print("Score = ",score_user,score_computer)
 
    elif computer_selection == "rock":
      ties =ties +1
      score_computer +=1
      print("Computer Won ")
      print("Score = ",score_user,score_computer)
  elif selection == "q" or selection == "Q":
    print("BYE BYE :))")
    break
  else:
    print("You entered incorrectly")
