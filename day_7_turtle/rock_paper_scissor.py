import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        user_input = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def display_choice(choice):
    ascii_art = {
        'rock': '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        ''',
        'paper': '''
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        ''',
        'scissors': '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''
    }
    return ascii_art[choice]

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Your choice:\n{display_choice(user_choice)}")
    print(f"Computer chose:\n{display_choice(computer_choice)}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
