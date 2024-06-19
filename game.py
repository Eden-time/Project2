import random

def get_guess(prompt):
    while True:
        try:
            guess = int(input(prompt))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = get_guess("Make a guess: ")
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low.")
        elif guess > number_to_guess:
            print("Too high.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    
    return attempts

def main():
    total_attempts = 0
    play_again = True
    
    while play_again:
        attempts = play_game()
        total_attempts += attempts
        
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'
    
    print(f"Total attempts across all games: {total_attempts}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
