class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def ask_question(self):
        question = self.questions[self.current_question_index]
        user_answer = input(question.prompt)
        if user_answer.lower() == question.answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {question.answer}.")
        self.current_question_index += 1

    def start(self):
        while self.current_question_index < len(self.questions):
            self.ask_question()
        print(f"Quiz finished! Your score is {self.score}/{len(self.questions)}.")

if __name__ == "__main__":
    questions = [
        Question("What is the capital of France? ", "Paris"),
        Question("What is 2 + 2? ", "4"),
        Question("What is the capital of Spain? ", "Madrid"),
        Question("What is the capital of Italy? ", "Rome"),
        Question("What is the capital of Germany? ", "Berlin")
    ]
    quiz = Quiz(questions)
    quiz.start()
