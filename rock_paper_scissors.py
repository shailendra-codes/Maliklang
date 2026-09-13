import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    score = {"player": 0, "computer": 0, "ties": 0}
    
    print("=" * 40)
    print(" Welcome to Rock, Paper, Scissors! ")
    print("=" * 40)
    
    while True:
        player_choice = input("\nEnter rock, paper, or scissors (or 'quit' to stop): ").lower().strip()
        
        if player_choice == 'quit':
            break
            
        if player_choice not in choices:
            print("Galat input! Kripya rock, paper, ya scissors likhein.")
            continue
            
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
            score["ties"] += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            score["player"] += 1
        else:
            print("Computer wins this round!")
            score["computer"] += 1
            
        print(f"\nScore -> You: {score['player']}, Computer: {score['computer']}, Ties: {score['ties']}")

    print("=" * 40)
    print(f"Thanks for playing! Final Score -> You: {score['player']}, Computer: {score['computer']}")
    print("=" * 40)

if __name__ == "__main__":
    play_game()
    
