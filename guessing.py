import random
from tkinter import messagebox as mb


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
        if self.rand_number == num:
            self.score += 1
            ask = mb.askyesno("Info", "Continue?")
            if ask:
                self.game_again(score_text, hint)
            else:
                exit(1)

    def game_again(self, score_text, hint):
        self.turn = 0
        self.rand_number = sel_num(self.mode)
        score_text.configure(text="Score: " + str(self.score))
        hint.configure(text="")