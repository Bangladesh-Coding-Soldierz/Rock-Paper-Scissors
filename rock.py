import random

def play_rock_paper_scissors():
    # The choices available in the game
    choices = ["rock", "paper", "scissors"]
    
    # The game introduction
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    
    while True:
        # Computer randomly selects its choice
        computer_choice = random.choice(choices)
        
        # User makes their choice
        user_choice = input("Choose your weapon [rock, paper, scissors]: ").lower()
        
        # Check if user's input is valid
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        print(f"Computer chose {computer_choice}.")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose.")
        
        # Ask the user if they want to play again
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break  # Exit the game loop if the user doesn't want to play again

if __name__ == "__main__":
    play_rock_paper_scissors()
