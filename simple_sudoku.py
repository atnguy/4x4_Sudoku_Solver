#the purpose of this code asides from solving simple 4x4 sudokus is to get myself famimliar with the python language and to practice implementing hill climbing search
import sys
import copy


def is_solution(board):
    #board is a 2d list full of integers from 0-4 represnting one row. with 0 representing an empty space. The size of board at this point is 4x4. It will not accept anything bigger or smaller.
    #returns the number of constraints the board fails to satisfy. The min number is 0, the max number should be 48. (16*3)
    #defintion of a constraint: number x should be in row y, number x should be in column y or number x should be in square y. There are 4 constraints for each row, column and square.
    #there are 4 rows, 4 columns and 4 squares. (4x4) + (4x4) +(4x4) = 16 + 16 + 16 = 48
    count = 0
    column = [[],[],[],[]]
    fourbyfour = [[],[],[],[]]
    rows = 0
    for row in board:
        if(1 not in row):
            count += 1
        if(2 not in row):
            count += 1
        if(3 not in row):
            count += 1
        if(4 not in row):
            count += 1
        for i in range(0,4):
            column[i].append(row[i])
            if(rows < 2):
                if(i < 2):
                    fourbyfour[0].append(row[i])
                else:
                    fourbyfour[1].append(row[i])
            else:
                if(i<2):
                    fourbyfour[2].append(row[i])
                else:
                    fourbyfour[3].append(row[i])
        rows += 1
    for columns in column:
        if(1 not in columns):
            count += 1
        if(2 not in columns):
            count += 1
        if(3 not in columns):
            count += 1
        if(4 not in columns):
            count += 1
    for square in fourbyfour:
        if(1 not in square):
            count += 1
        if(2 not in square):
            count += 1
        if(3 not in square):
            count += 1
        if(4 not in square):
            count += 1
    return count

def is_full(board):
    #returns whether or not the board is full of numbers that are not 0
    #I believe this is a linear runtime
    for row in board:
        if(0 in row):
            return False
        if(len(row) != 4):
            print("invalid board\n")
            return False
    return True

def print_board(board):
    #prints the board as it is
    #primarily used as a debugging tool
    for row in board:
        line = ""
        for entry in row:
            line = line + str(entry) + " "
        print(line)

def solve_board_simple(board,iteration = 0):
    #use hill climbing to return either a solved board or an error when the algorithm reached an unsolveable board.
    #upon arriving at a local maxima, the algorithm will attempt to backtrack and use the next successor. If all successors have been discarded due to a local maxima, it will attempt to
    #undo a step (aka go back one step in the recursion). If it cannot do that then it returns an error
    #Hill climbing is performed by examining each blank entry and trying to place a number in there that would satisfy the most contstaints. Then recursively call this function
    #until a solution or error is reached
    if(is_solution(board) == 0):
        return board
    for row in range(0,4):
        for entry in range(0,4):
            if(board[row][entry] == 0):
                #the 4 states the current state can move into
                
                replace_one = copy.deepcopy(board)
                replace_one[row][entry] = 1
                
                replace_two = copy.deepcopy(board)
                replace_two[row][entry] = 2
                
                replace_three = copy.deepcopy(board)
                replace_three[row][entry] = 3
                
                replace_four = copy.deepcopy(board)
                replace_four[row][entry] = 4

                current_heuristic = is_solution(board)
                
                heuristic_one = is_solution(replace_one)
                heuristic_two = is_solution(replace_two)
                heuristic_three = is_solution(replace_three)
                heuristic_four = is_solution(replace_four)
                
                successor = min([current_heuristic,heuristic_one,heuristic_two,heuristic_three,heuristic_four])
                if(successor == current_heuristic):
                    #note: if the min successor heuristic is equivalent to the current state heuristic, this if condition is going to go here.
                    #not sure what to do with about this interaction, decided to treat the current state as the "best" state to be in for the time being.
                    #because it stops potential infinte loops from happening because I don't track if a state was visited.
                    return board
                else:
                    answers = {
                        heuristic_one: replace_one,
                        heuristic_two: replace_two,
                        heuristic_three: replace_three,
                        heuristic_four: replace_four,
                    }
                    answer = solve_board_simple(answers[successor],iteration+1)
                    if(is_solution(answer) != 0):
                        del answers[successor]
                        for successors in answers:
                            attempt = solve_board_simple(successors,iteration+1)
                            if(is_solution(successors) == 0):
                                return successors
                        if(iteration > 0):
                            return board
                        raise ValueError("This board is not solveable")
                    else:
                        return answer
            else:
                #skipping
                continue
    #assumes that the board is full and not solveable because of an invalid entry or a local maxima was reached
    if(iteration > 0):
        return board
    raise ValueError("This board is not solveable")