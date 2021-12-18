from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f'this is a test',
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        image_true = PhotoImage(file="images/true.png")
        image_false = PhotoImage(file="images/false.png")
        self.lable_t = Label(text="score:", highlightthickness=0, bg=THEME_COLOR, fg="white", font=("Arial", 15, ""))
        self.lable_t.grid(column=1, row=0)
        self.true_button = Button(
            image=image_true,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.answer_ture
        )
        self.true_button.grid(column=0, row=2 )
        self.false_button = Button(
            image=image_false,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.answer_false
        )
        self.false_button.grid(column=1, row=2, )
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lable_t.config(text=f"{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text= "you have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def answer_ture(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
