from tkinter import *

from database import DB
from guessing import Game
from rd_button import RdButton as rd_btn
from tkinter import messagebox as mb

screen = Tk()
screen.geometry('800x800')
screen.title("Guessing")

Label(text="Guess number", font=("Arial", 25)).place(x=300, y=10)
modes = ['easy', 'medium', 'hard']

score_text = Label(text="Score: 0", font=("Arial", 20))
score_text.place(x=650, y=40)

Label(text="Best scores", font=("Arial", 20)).place(x=50, y=50)
listbox = Listbox(font=("Arial", 15), height=15, width=15)
listbox.place(x=50, y=100)

var = IntVar()
var.set(0)

rd_btn(lambda: radio_check(modes[0]), modes[0], 280, 60, var)
rd_btn(lambda: radio_check(modes[1]), modes[1], 370, 60, var)
rd_btn(lambda: radio_check(modes[2]), modes[2], 480, 60, var)

Label(text="Write your username", font=("Arial", 20)).place(x=280, y=110)
user_entry = Entry(font=("Arial", 20))
user_entry.place(x=280, y=150)
Button(text="Start", font=("Arial", 20), width=17, command=lambda: start_game()).place(x=290, y=200)

i_mode = IntVar()
i_mode.set(-1)

desc = Label(font=("Arial", 15))
desc.place(x=280, y=280)

hint = Label(font=("Arial", 15))
hint.place(x=290, y=520)

Label(text="""EASY - the number range is selected 0 - 10
    MEDIUM - the number range is selected 0 - 20
HARD - the number range is selected 0 - 30""",
      font=("Arial", 15)).place(x=220, y=600)


def start_game():
    username = user_entry.get()
    if username == '':
        mb.showerror("Error", "Fill the username")
    if i_mode.get() == -1:
        mb.showerror("Error", "Change the mode")
    else:
        game = Game(i_mode.get(), username)
        Label(text=username + ", guess number", font=("Arial", 15)).place(x=280, y=350)
        user_entry.delete(0, END)
        guess_entry = Entry(font=("Arial", 20))
        guess_entry.place(x=280, y=400)
        Button(text="Guess!!!", font=("Arial", 20), width=17,
               command=lambda: game.guess(int(guess_entry.get()), score_text, hint)).place(x=290, y=450)


def radio_check(mode):
    desc.configure(text="The selected mode is " + mode)
    if mode == "easy":
        i_mode.set(1)
    if mode == "medium":
        i_mode.set(2)
    if mode == "hard":
        i_mode.set(3)


db = DB()
for item in db.select_value():
    listbox.insert(END, f"{item[0]}: {item[1]}")

screen.mainloop()
