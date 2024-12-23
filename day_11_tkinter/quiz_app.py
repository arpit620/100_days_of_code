import tkinter as tk
from tkinter import messagebox
import requests
import html

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.score = 0
        self.current_question = 0
        self.questions = []
        self.create_widgets()
        self.load_questions()
        self.display_question()

    def load_questions(self):
        response = requests.get("https://opentdb.com/api.php?amount=10&type=multiple")
        if response.status_code == 200:
            data = response.json()
            self.questions = data['results']
        else:
            messagebox.showerror("Error", "Failed to fetch questions")
            self.root.quit()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            # Replace HTML special characters in the question and answers using html.unescape
            question_text = html.unescape(question['question'])
            self.question_label.config(text=question_text)
            self.score_label.config(text=f"Score: {self.score}/{self.current_question}")
            answers = [html.unescape(answer) for answer in question['incorrect_answers']]
            correct_answer = html.unescape(question['correct_answer'])
            answers.append(correct_answer)
            import random
            random.shuffle(answers)
            for i, answer in enumerate(answers):
                self.buttons[i].config(text=answer, command=lambda ans=answer, btn=self.buttons[i]: self.check_answer(ans, btn))
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(self.questions)}")
            self.root.quit()

    def check_answer(self, answer, button):
        question = self.questions[self.current_question]
        if answer == question['correct_answer']:
            self.score += 1
            button.config(bg="green")
        else:
            button.config(bg="red")
        self.root.update()  # Force the GUI to update immediately
        self.root.after(1000, self.next_question)  # Wait for 1 second before moving to the next question

    def next_question(self):
        self.current_question += 1
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text="Score: 0/0")
        self.score_label.pack(pady=10)

        self.buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", width=40, command=lambda: None)
            button.pack(pady=5)
            self.buttons.append(button)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
