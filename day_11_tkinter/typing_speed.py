import tkinter as tk
import time

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.start_time = None
        
        self.label = tk.Label(root, text="Type the following text:")
        self.label.pack()
        
        self.sample_label = tk.Label(root, text=self.sample_text, wraplength=400)
        self.sample_label.pack()
        
        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack()
        self.text_entry.bind("<KeyPress>", self.start_timer)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.check_button = tk.Button(root, text="Check Speed", command=self.check_speed)
        self.check_button.pack()
    
    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()
    
    def check_speed(self):
        end_time = time.time()
        time_taken = end_time - self.start_time
        typed_text = self.text_entry.get()
        
        if typed_text == self.sample_text:
            words_per_minute = len(typed_text.split()) / (time_taken / 60)
            self.result_label.config(text=f"Typing Speed: {words_per_minute:.2f} WPM")
        else:
            self.result_label.config(text="Text does not match. Try again.")
        
        self.start_time = None

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
