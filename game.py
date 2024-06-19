import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = input("Make a guess: ")
        
        # Ensure the input is an integer
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low.")
        elif guess > number_to_guess:
            print("Too high.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    number_guessing_game()
