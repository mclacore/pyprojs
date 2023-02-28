import random

while True:
  user = input("Pick your weapon: rock, paper, or scissors): ")
  options = ["rock", "paper", "scissors"]
  computer = random.choice(options)
  print(f"\nYou picked {user}, computer picked {computer}.\n")
  if user == computer:
    print("It's a tie!")
  if (user == "rock" and computer == "paper") or (user == "paper" and computer == "scissors") or (user == "scissors" and computer == "rock"):
    print("You lost!")
  if (computer == "rock" and user == "paper") or (computer == "paper" and user == "scissors") or (computer == "scissors" and user == "rock"):
    print("You've won!")

  play_again = input("Want to play again? (y/n): ")
  if play_again.lower() != "y":
    break