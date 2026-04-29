import random

def get_computer_pick():
    options = ["Stone", "Paper", "Scissors"]
    return random.choice(options)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    
    if (user == "Stone" and computer == "Scissors") or \
       (user == "Paper" and computer == "Stone") or \
       (user == "Scissors" and computer == "Paper"):
        return "user"
    else:
        return "computer"

def play_game():
    
    user_score = 0
    computer_score = 0
    draw_score=0
    choice2 = {"1": "Stone", "2": "Paper", "3": "Scissors"}
    print("--- Welcome to Stone-Paper-Scissors ---")
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Play Round")
        print("2. View Score")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
       
        if choice == '1':
            print("\nPick your move:")
            print("1. Stone")
            print("2. Paper")
            print("3. Scissors")

            inputchoice= input("Enter your move:(1, 2 or 3): ")    
            
            if inputchoice not in choice2:
                print("Invalid input! Try from the mentioned choices.")
                continue
            
            user_pick = choice2[inputchoice]
            comp_pick = get_computer_pick()
            print(f"Computer chose: {comp_pick}")
            
        
            result = determine_winner(user_pick, comp_pick)
            
            if result == "user":
                print("YAYY YOU WINN!")
                user_score += 1
            elif result == "computer":
                print("YOU LOSEEE!")
                computer_score += 1
            else:
                print("It's a draw! YUCKK. ")
                draw_score += 1
                
                
        elif choice == '2':
            print("\n--- CURRENT SCORE ---")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            print(f"Draws: {draw_score}")
            
        elif choice == '3':
            print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! Tataaaa!!.")
            break
        else:
            print("Invalid choice, please pick 1, 2, or 3.")

if __name__ == "__main__":
    play_game()
