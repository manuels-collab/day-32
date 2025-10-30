from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = '#FFFFFF'


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=340, height=500)
        self.window.config(bg=THEME_COLOR)
        self.score_text = Label(text=f'Score: 0', bg=THEME_COLOR, fg=WHITE, pady=20)
        self.score_text.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(
            150 ,
            125,
            width=280,
            text="Random Text",
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=1, columnspan=2, padx=20)
        check_button = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=check_button, command=self.is_right)
        self.true_button.grid(row=2, column=1, pady=40)
        unchecked_button = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=unchecked_button, command=self.is_wrong)
        self.false_button.grid(row=2, column=2, pady=40)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.confif(state="disabled")

    def is_right(self):
        self.give_feedback(self.quiz.check_answer('True'))



    def is_wrong(self):
        is_wrong = self.quiz.check_answer('False')
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)










