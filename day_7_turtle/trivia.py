import requests
import json
import random
import html  # Add this import


def get_trivia_questions():
    url = "https://opentdb.com/api.php?amount=5&type=multiple"
    response = requests.get(url)
    data = response.json()
    return data['results']

def ask_question(question_data):
    question = html.unescape(question_data['question'])  # Unescape HTML entities
    correct_answer = html.unescape(question_data['correct_answer'])  # Unescape HTML entities
    incorrect_answers = [html.unescape(ans) for ans in question_data['incorrect_answers']]  # Unescape HTML entities
    options = incorrect_answers + [correct_answer]
    random.shuffle(options)
    
    print(f"Question: {question}")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    answer = int(input("Your answer (1-4): "))
    if options[answer - 1] == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was: {correct_answer}")

def main():
    questions = get_trivia_questions()
    for question_data in questions:
        ask_question(question_data)

if __name__ == "__main__":
    main()
