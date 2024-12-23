import tkinter as tk
from tkinter import messagebox
import random

class FlashCardApp:
    def __init__(self, root):
        self.root = root  # root is the main window of the application
        self.root.title("Flash Card App")
        self.root.geometry("400x300")

        self.flash_cards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is the color of the sky on a clear day?", "answer": "Blue"}
        ]

        self.current_card = None
        

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        

        self.answer_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.answer_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Card", command=self.show_question)
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        self.current_card = random.choice(self.flash_cards)
        self.question_label.config(text=self.current_card["question"])
        self.answer_button.config(state=tk.NORMAL)

    def show_answer(self):
        self.question_label.config(text=self.current_card["answer"])
        self.answer_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = FlashCardApp(root)  # Initialize the FlashCardApp with the main window
    root.mainloop()  # Start the Tkinter event loop
