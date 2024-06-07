import random
print("Welcome to Rock Paper Scissors")
player_choice = input("Choose Rock, Paper, or Scissors: ")
computer_choice = random.choice(["Rock", "Paper", "Scissors"]).lower()

print("Computer chose " + computer_choice)

if player_choice.lower() == computer_choice:
	    print("It's a tie!")

    elif (player_choice.lower() == "rock" and computer_choice == "scissors") or (player_choice.lower() == "paper" and computer_choice == "rock") or (player_choice.lower() == "scissors" and computer_choice == "paper"):

	    print("Player wins!")

	else:
		print("Computer wins!")
		print("Thanks for playing!")  [end of text]
