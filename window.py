import sys
import simple_sudoku as ss
from tkinter import *


class Sudoku(Frame):
    def solve_sudoku(self):
        try:
            board = [[],[],[],[]]
            i = 0
            for row in self.entry_list:
                j = 0
                for entry in row:
                    number = self.entry_list[i][j].get()
                    if(number.isdigit()): 
                        board[i].append(int(number))
                    elif(len(number) == 0):
                        board[i].append(0)
                    else:
                        self.message_widget.configure(text ="Your input does not exclusively contain numbers, please try again with a different input")
                        return
                    j += 1
                i += 1
            board = ss.solve_board_simple(board)
            for x in range(0,4):
                for y in range(0,4):
                    self.entry_list[x][y].delete(0,END)
                    number = str(board[x][y])
                    self.entry_list[x][y].insert(0,number)
            self.message_widget.configure(text = "Sovled!")
            return
        except ValueError:
            self.message_widget.configure(text = "This board is not solveable, please try a differnt board")
            return
    def createWidgets(self):
        self.Title_frame = Frame()
        #The title
        self.title = Label(master=self.Title_frame,text="Sudoku Solver",width = 20, height = 5)
        self.title.pack()
        self.Title_frame.pack()
        
        #the instructions message widget, it changes based on the input provided
        self.message_frame = Frame()
        self.message_widget = Message(self.message_frame,text = "Use the 16 boxes below to input numbers from 1-4 for a 4x4 sudoku board.\n It will try to solve the board for you provided that it is not completely full and return a possible solution.", width = 1000,justify = LEFT)
        self.message_widget.pack()
        self.message_frame.pack()
        
        #the board
        #consists of 16 entry widgests stored in entry_list. There are 4 entries in each row. Each row has its own frame stored in entry_frames
        for i in range(0,4):
            tempframe = Frame()
            self.entry_frames.append(tempframe)
            for j in range(0,4):
                temp = Entry(master=self.entry_frames[i], bd = 5)
                self.entry_list[i].append(temp)
                self.entry_list[i][j].pack(side = RIGHT)
            self.entry_frames[i].pack()
        
        #The solve button
        self.solve_button_frame=Frame(bd = 5)
        self.solve_button = Button(master =self.solve_button_frame)
        self.solve_button["text"] = "Solve Sudoku"
        self.solve_button["fg"] = "green"
        self.solve_button["command"] = self.solve_sudoku
        self.solve_button.pack()
        self.solve_button_frame.pack()
    
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.pack()
        self.entry_frames = []
        self.entry_list = [[],[],[],[]]
        self.createWidgets()
root = Tk()
window = Sudoku(master = root)
window.mainloop()