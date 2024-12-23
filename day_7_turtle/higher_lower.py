import random

def higher_lower_game():
    print("Welcome to the Higher or Lower Game!")
    current_number = random.randint(1, 100)
    score = 0

    while True:
        print(f"Current number: {current_number}")
        guess = input("Will the next number be higher or lower? (h/l): ").lower()

        if guess not in ['h', 'l']:
            print("Invalid input. Please enter 'h' for higher or 'l' for lower.")
            continue

        next_number = random.randint(1, 100)
        print(f"Next number: {next_number}")

        if (guess == 'h' and next_number > current_number) or (guess == 'l' and next_number < current_number):
            score += 1
            print("Correct! Your score is:", score)
        else:
            print("Wrong! Game over. Your final score is:", score)
            break

        current_number = next_number

if __name__ == "__main__":
    higher_lower_game()
