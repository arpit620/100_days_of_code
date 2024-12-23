import random

# List of words to choose from
words = ['python', 'hangman', 'challenge', 'developer', 'programming']

# Function to select a random word
def choose_word(word_list):
    return random.choice(word_list)

# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game function
def hangman():
    word_to_guess = choose_word(words)
    guessed_letters = set()
    attempts_remaining = 6
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts_remaining > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            attempts_remaining -= 1
            print(f"Incorrect! Attempts remaining: {attempts_remaining}")
            print(hangman_stages[6 - attempts_remaining])

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if '_' not in current_display:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Game over! The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
