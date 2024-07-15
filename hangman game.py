import random

# List of words for the game
words = ["python", "development", "hangman", "programming", "interface"]

def choose_word():
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 6
    wrong_guesses = set()
    
    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        print("\n" + display_current_state(word, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        print(f"Wrong guesses: {', '.join(wrong_guesses)}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters or guess in wrong_guesses:
            print("You've already guessed that letter. Try again.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            wrong_guesses.add(guess)
            attempts_left -= 1
            print("Incorrect guess.")
        
        if attempts_left == 0:
            print("\nSorry, you've run out of attempts. The word was:", word)

# Run the game
hangman()
