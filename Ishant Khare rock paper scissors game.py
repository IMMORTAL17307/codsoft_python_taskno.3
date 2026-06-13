import random

ROCK_ART = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER_ART = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS_ART = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def print_hand(choice):
    if choice == "rock":
        print(ROCK_ART)
    elif choice == "paper":
        print(PAPER_ART)
    elif choice == "scissors":
        print(SCISSORS_ART)

def play_game():

    print("==========================================")
    print("       ROCK-PAPER-SCISSORS SHOWDOWN       ")
    print("==========================================")
    print("Instructions:")
    print("  - Choose: rock, paper, or scissors")
    print("  - Rules: Rock beats Scissors")
    print("           Scissors beats Paper")
    print("           Paper beats Rock")
    print("==========================================")
    
  
    user_score = 0
    computer_score = 0
    ties = 0

    choices = ["rock", "paper", "scissors"]

    while True:
        
        user_choice = input("\nEnter choice (rock/paper/scissors): ").strip().lower()
        
        if user_choice not in choices:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)

        print("\nYour choice:")
        print_hand(user_choice)
        print("Computer's choice:")
        print_hand(computer_choice)

        if user_choice == computer_choice:
            print("Outcome: It's a tie!")
            ties += 1
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Outcome: You win! (Rock crushes Scissors)")
                user_score += 1
            else:
                print("Outcome: Computer wins! (Paper covers Rock)")
                computer_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Outcome: You win! (Paper covers Rock)")
                user_score += 1
            else:
                print("Outcome: Computer wins! (Scissors cut Paper)")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Outcome: You win! (Scissors cut Paper)")
                user_score += 1
            else:
                print("Outcome: Computer wins! (Rock crushes Scissors)")
                computer_score += 1

        print(f"\nScoreboard -> You: {user_score} | Computer: {computer_score} | Ties: {ties}")
        print("------------------------------------------")

        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes" and play_again != "y":
            break

    print("\n==========================================")
    print("            FINAL GAME OVER SUMMARY       ")
    print("==========================================")
    print(f"Total Wins by You      : {user_score}")
    print(f"Total Wins by Computer : {computer_score}")
    print(f"Total Ties             : {ties}")
    print("------------------------------------------")
    if user_score > computer_score:
        print("Overall Result: Congratulations! You won! 🏆")
    elif user_score < computer_score:
        print("Overall Result: Computer won the game. 🤖")
    else:
        print("Overall Result: It ended in a draw! 🤝")
    print("==========================================\n")

if __name__ == "__main__":
    play_game()
