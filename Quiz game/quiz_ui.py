import tkinter
from tkinter import Tk, Canvas, StringVar, Radiobutton, Label, Button, messagebox
from quiz_brain import QuizBrain
class Quiz_Ui:
    def __init__(self,quiz_brain: QuizBrain) ->None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.geometry("1080x720")
        self.window.title('The Quiz Game')
        self.window.title()
        self.display_title()

        self.canvas = Canvas()
        self.question_text =self.canvas.create_text(400, 125, text='question here',width = 700, fill = '#4f819c', font = ('Roboto', 20, 'normal'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()
        self.u_answer = StringVar()
        self.options =self.radio_buttons()
        self.buttons()
        self.fb = Label(self.window, pady=10, font=('Roboto', 18, 'Bold'))
        self.fb.place(x = 300, y =400)
        self.window.mainloop()
    def display_question(self):
        qtext =self.quiz.go_to_next()
        self.canvas.itemconfig(self.question_text, text = qtext)
    def display_title(self):
        title = Label(self.window, text='Quiz Game', width= 50, bg='green', fg = 'White', font=('Roboto', 20, 'bold')).place(x = 0, y =2 )
    def radio_buttons (self): 
        MC_list = []
        y_pos = 200
        while len(MC_list)< 4:
            choice =  Radiobutton(self.window, text='', variable=self.u_answer, value='', font=('Roboto', 14))
            MC_list.append(choice)
            choice.place(x=200, y= y_pos)
            y_pos += 50
        return MC_list
    def display_answers(self):
        value = 0
        self.u_answer.set(None)
        for option in self.quiz.currentque.choices:
            self.options[value]['text'] = option
            self.options[value]['value'] = option
            value +=1
    def next_button(self):
        if self.quiz.check_answer(self.u_answer.get()):
            self.fb['fg']= 'green'
            self.fb['text'] = "Correct!!!!!!"
        else:
            self.fb['fg'] = 'red'
            self.fb['text'] =('wrong!\n' f'the right answer is {self.quiz.currentque.correct_answer}')
        if self.quiz.still_more():
            self.display_question()
            self.display_answers()
        else:
            self.display_result()
            self.window.destroy()
    def buttons(self):
        next_button = Button(self.window, text='Next', command=self.next_button(), width=10, bg='green', fg='white', font=('Roboto', 18, 'bold')).place(x=350, y= 460)
        quit_button = Button(self.window, text='Quit', command=self.window.destroy(), width=10, bg='red', fg='white', font=('Roboto', 18, 'bold')).place(x=700, y= 50)
    def display_result(self):
        corr_num, wr_num, sc_pc = self.quiz.get_score()
        correct = f"Correct Answers: {corr_num}"
        Wrong = f"Wrong Answers: {wr_num}"
        result = f"Score: {sc_pc}%"
        messagebox.showinfo("Result", f"{correct}\n{Wrong}\n{result}")


