import random

print("🎮 Number Guessing Game")
print("I'm thinking of a number 1-20...")

secret = random.randint(1,20)
guesses = 0
lives = 5

while lives > 0:
    guess = int(input(f"Guess ({lives} lives left): "))
    guesses += 1

    if guess < secret:
         print("📈 Too LOW")
         lives -= 1
    elif guess > secret:
         print("📉 Too HIGH")
         lives -= 1
    else:
         print(f"🎉 WIN! {guesses} guesses used!")
         break
    
if lives == 0:
     print(f"💀 Game Over! It was {secret}")

play_again = input("Play again? (y/n): ")
print("Great game!")
