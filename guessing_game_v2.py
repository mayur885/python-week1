import random

while True: # 🔄 Play forever!
    print("\n🎮 Number Guessing Game")
    print("I'm thinking of 1-20...")

    secret =random.randint(1,20)
    guesses = 0
    lives = 5

    while lives > 0:
        guess = int(input(f"Guess ({lives} lives): "))
        guesses += 1

        if guess < secret:
            print("📈 Too LOW")
            lives -= 1
        elif guess > secret:
            print("📉 Too HIGH")
            lives -= 1
        else:
            print(f"🎉 WIN! {guesses} guesses ({secret} was it)!")
            break

    if lives == 0:
        print(f"💀 Lost! Answer was {secret}")

    # Ask to continue
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y' :
        print("👋 Thanks for playing!")
        break
    
