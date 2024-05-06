import tkinter as tk
from tkinter import messagebox
from functools import partial
import random

class PuzzleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("8 Puzzle Game")
        self.master.resizable(False, False)

        self.tiles = []
        self.empty_pos = (2, 2)  # Initial empty position

        self.init_board()
        self.shuffle_board()

    def init_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                tile = tk.Button(self.master, text='', width=5, height=2,
                                 font=('Helvetica', 20, 'bold'),
                                 command=partial(self.move_tile, (i, j)))
                tile.grid(row=i, column=j, padx=2, pady=2)
                row.append(tile)
            self.tiles.append(row)

    def shuffle_board(self):
        numbers = list(range(1, 9))
        random.shuffle(numbers)

        for i in range(3):
            for j in range(3):
                if i == 2 and j == 2:
                    self.tiles[i][j].config(text='')
                    self.empty_pos = (i, j)
                else:
                    num = numbers.pop()
                    self.tiles[i][j].config(text=num)

    def move_tile(self, pos):
        row, col = pos
        if self.is_adjacent(pos, self.empty_pos):
            self.tiles[self.empty_pos[0]][self.empty_pos[1]].config(text=self.tiles[row][col]['text'])
            self.tiles[row][col].config(text='')
            self.empty_pos = pos
            if self.is_solved():
                self.master.after(100, lambda: messagebox.showinfo("Congratulations!", "You solved the puzzle!"))


    def is_adjacent(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2) == 1

    def is_solved(self):
        numbers = [self.tiles[i][j]['text'] for i in range(3) for j in range(3)]
        return numbers == ['1', '2', '3', '4', '5', '6', '7', '8', '']

root = tk.Tk()
game = PuzzleGame(root)
root.mainloop()
