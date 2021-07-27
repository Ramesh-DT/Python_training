import random

print("rock, paper, scissors...")


def play():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    player = input("Enter your choice: ").lower()
    print(f"You chose {player} and computer chose {computer} ")

    if player == computer:
        print(f"Both players selected {player}. It's a tie!!!")
    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!!!")
        else:
            print("Paper covers rock! You lose.")
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!!!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!!!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Please give proper input")
    play_again = input("Do you want to play again? yes or no: ").lower()
    if play_again == "yes":
        play()
    elif play_again == "no":
        print("Goodbye")


play()
