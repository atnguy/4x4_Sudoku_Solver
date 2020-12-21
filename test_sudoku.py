import simple_sudoku
valid_board = [[1,3,2,4],[2,4,3,1],[3,1,4,2],[4,2,1,3]]
invalid_solution = [[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]]

#basic unit tests
def test_is_solution():
    #a basic test for is_solution
    assert simple_sudoku.is_full(valid_board) == True, "Should be True"
    assert simple_sudoku.is_solution(valid_board) == 0, "Should be 0"
    assert simple_sudoku.is_full(invalid_solution) == True, "Should be True"
    assert simple_sudoku.is_solution(invalid_solution) == 4, "Should be 4"

def test_print():
    simple_sudoku.print_board(valid_board)

def test_solver():
    assert simple_sudoku.solve_board_simple(valid_board) == valid_board, "Should remain the same"
    missing_one_board = [[0,3,2,4],[2,4,3,1],[3,1,4,2],[4,2,1,3]]
    answer = simple_sudoku.solve_board_simple(missing_one_board)
    assert  answer == valid_board, "Should find the solution"
    missing_one_row = [[0,0,0,0],[2,4,3,1],[3,1,4,2],[4,2,1,3]]
    assert simple_sudoku.solve_board_simple(missing_one_row) == valid_board, "Should find the solution"

if __name__ == "__main__":
    test_is_solution()
    #test_print()
    test_solver()
    print("Everything passed")
    