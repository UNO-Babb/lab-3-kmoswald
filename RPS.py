#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  playAgain = "Y"
  while playAgain == "Y":
  
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice( ["R", "P", "S"] )
    #Prompt the user for their RPS selection
    player = input("Pick your weapon (R, P, S): ")
    
    #Determine winner and state what happened to the user
    if computer == "R":
        print("Computer chose Rock")
        if player == "R":
           ties = ties + 1
           print("Tie")
        elif player == "P":
           wins = wins + 1
           print("You win!")
        else:
           losses = losses + 1
           print("Computer wins.")

    elif computer == "P":
        print("Computer chose Paper")
        if player == "R":
           losses = losses + 1
           print("Computer wins.")
        elif player == "P":
           ties = ties + 1
           print("Tie")
        else:
           wins = wins + 1
           print("You win!")
    # Computer chose scissors
    else:
      print ("Computer chose scissors")
      if player == "R":
           wins = wins + 1
           print("You win!")
      elif player == "P":
          losses = losses + 1
          print("Computer wins.")
      else:
          ties = ties + 1
          print("Tie")

    #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

    #Ask the user if they would like to play again.
    playAgain = input("Play again? (Y/N): ")
  
  

if __name__ == '__main__':
  main()
