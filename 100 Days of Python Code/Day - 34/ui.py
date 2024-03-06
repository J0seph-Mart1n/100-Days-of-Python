import tkinter
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.brain = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quiz App")
        self.window.minsize(height=500,width=340)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = tkinter.Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 15), fg="white")
        self.score.grid(row=0, column=1, padx=20, pady=20)
        self.canvas = tkinter.Canvas(width=300, height=250)
        self.q_text = self.canvas.create_text(150,125,width=280,text="Question Bank", font=("Arial", 15, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, columnspan=2, padx=20, pady=20)
        self.right = tkinter.PhotoImage(file="images/true.png")
        self.wrong = tkinter.PhotoImage(file="images/false.png")
        self.right_button = tkinter.Button(image=self.right, command=self.right_func)
        self.right_button.grid(row=3, column=0, padx=20, pady=20)
        self.wrong_button = tkinter.Button(image=self.wrong, command=self.wrong_func)
        self.wrong_button.grid(row=3, column=1, padx=20, pady=20)
        self.get_next_que()
        self.window.mainloop()

    def get_next_que(self):
        self.canvas.config(bg="white")
        if self.brain.still_has_questions():
            self.score.config(text=f"Score: {self.brain.score}")
            question = self.brain.next_question()
            self.canvas.itemconfig(self.q_text, text=question)
        else:
            self.canvas.itemconfig(self.q_text, text="Your quiz is over")
            self.score.config(text=f"Score: {self.brain.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def right_func(self):
        answer = self.brain.check_answer("True")
        if answer:
            self.green_canvas()
        else:
            self.red_canvas()
        self.give_feedback()

    def wrong_func(self):
        answer = self.brain.check_answer("False")
        if answer:
            self.green_canvas()
        else:
            self.red_canvas()
        self.give_feedback()

    def green_canvas(self):
        self.canvas.config(bg="green")

    def red_canvas(self):
        self.canvas.config(bg="red")

    def give_feedback(self):
        self.window.after(1000, self.get_next_que)
