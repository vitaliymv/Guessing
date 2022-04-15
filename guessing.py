import random
from tkinter import messagebox as mb

from database import DB


def sel_num(mode):
    return random.randint(0, 10 * mode)


class Game:
    def __init__(self, mode, username):
        self.mode = mode
        self.username = username
        self.rand_number = sel_num(self.mode)
        self.turn = 0
        self.score = 0

    def guess(self, num, score_text, hint):
        db = DB()
        if self.rand_number == num:
            self.score += 1
            ask = mb.askyesno("Info", "Continue?")
            if ask:
                self.game_again(score_text, hint)
            else:
                db.insert_value(self.username, self.score)
                exit(1)
        else:
            self.turn += 1
            if num > self.rand_number:
                hint.configure(text="Your number greater", fg="red")
            elif num < self.rand_number:
                hint.configure(text="Your number less", fg="red")
            if self.turn == 3:
                if self.rand_number % 2 == 0:
                    hint.configure(text="My number is even", fg="blue")
                else:
                    hint.configure(text="My number is odd", fg="blue")
            elif self.turn == 4:
                ask = mb.askyesno("Info", "Restart?")
                if ask:
                    db.insert_value(self.username, self.score)
                    self.score = 0
                    self.game_again(score_text, hint)
                else:
                    db.insert_value(self.username, self.score)
                    exit(1)

    def game_again(self, score_text, hint):
        self.turn = 0
        self.rand_number = sel_num(self.mode)
        score_text.configure(text="Score: " + str(self.score))
        hint.configure(text="")