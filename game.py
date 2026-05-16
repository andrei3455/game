import random as rnd

choices = ["rock", "paper", "scissor"]
round_count = 0
player_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")
print("The game will run for 10 rounds, or type 'quit' to exit early.\n")

while round_count < 10:
    print(f"--- Round {round_count + 1} of 10 ---")
    player = input("Pick (rock, paper, scissor): ").lower()
    
    if player == 'quit':
        print("\nExiting game early.")
        break
        
    if player not in choices:
        print("Invalid choice! Try again.\n")
        continue

    round_count += 1
    computer = rnd.choice(choices)
    print(f"Computer picked: {computer}")

    if player == computer:
        print("Result: tit-\n")
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        print("Result: magaling ka ah\n")
        player_score += 1
    else:
        print("Result: naol bonak\n")
        computer_score += 1

print("=== FINAL SCORE ===")
print(f"You: {player_score} | Computer: {computer_score}")
if player_score > computer_score:
    print("Congratulations! You won the match! ")
elif player_score < computer_score:
    print("The computer won the match! Better luck next time. ")
else:
    print("The match ended in a tie! ")
