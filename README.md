# 4x4_Sudoku_Solver
This program creates a window where you can input a 4x4 sudoku board and the program will try to solve it.

## Files

### simple_sudoku.py
This file is the bulk of the project, contains the functions and algorithm that solves the sudoku board.

### test_sudoku.py
This file just contains some basic testing I did for simple_sudoku.py to ensure that it works.
This file is optional and is not required to run the program successfully

### window.py
This file uses tkinter to create a gui interface where you can input a 4x4 sudoku board that the program needs to solve. Provides messages for when the board is solved, not solved or invalid input

## How to use
Once you have at least simple_sudoku.py and window.py, run window.py and you'll encounter this interface
![alt text](https://i.imgur.com/Co17kSG.png)

Fill in as many boxes with numbers between 1-4 and press the "Solve sudoku" button when ready (Note: the image above represents the first iteration of this project so the current interface may not look like that at all)

## Status
I will probably not any improvements to the algorithm unless there is a bug which I did not encounter when testing and decide what to do with it.

I will try to make improvements to the interface in my spare time. However, I will continue to use tkinter as the interface.
