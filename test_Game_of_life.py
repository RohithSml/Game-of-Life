#Testing file for Game_of_life.py
import Game_of_life


"""1.Creating a nxn matrix
2.Initilize predefined live cells
3.Check is cell is alive
4.Kill the cell
5.Give life to cell
6.Return number of neighbours
7.Apply rules
"""
def test_3x3_matrix():
    expected_value=[[0,0,0],[0,0,0],[0,0,0]]
    assert Game_of_life.matrix(3) == expected_value

def test_initializing_predefined_live_cells():
    matrix=[[0,0,0],[0,0,0],[0,0,0]]
    expected_value= [[0,1,0],[0,1,0],[0,1,0]]
    assert Game_of_life.initial(matrix)== matrix
    
def test_for_cell_alive():
    matrix=[[0,1,0],[0,1,0],[0,1,0]]
    assert Game_of_life.alive(matrix[0][1])==True
    assert Game_of_life.alive(matrix[1][1])==True
    assert Game_of_life.alive(matrix[2][1])==True

def test_for_killing_cell():
    matrix=[[1,1,0],[0,0,1],[0,0,1]]
    Game_of_life.die(matrix, 0, 1)
    assert matrix == [[1,0,0],[0,0,1],[0,0,1]]
    Game_of_life.die(matrix, 0, 0)
    assert matrix == [[0,0,0],[0,0,1],[0,0,1]]
    Game_of_life.die(matrix, 0, 2)
    assert matrix == [[0,0,0],[0,0,1],[0,0,1]]

def test_for_giving_life_to_cell():
    matrix=[[0,0,1],[0,0,1],[0,0,1]]
    Game_of_life.live(matrix, 0, 1)
    assert matrix == [[0,1,1],[0,0,1],[0,0,1]]
    Game_of_life.live(matrix, 0, 0)
    assert matrix == [[1,1,1],[0,0,1],[0,0,1]]
    Game_of_life.live(matrix, 1, 2)
    assert matrix == [[1,1,1],[0,0,1],[0,0,1]]

def test_for_returning_number_of_alive_neighbours():
    matrix=[[0,1,0],
            [0,1,0],
            [0,1,0]]
    assert Game_of_life.alive_neighbour(matrix, 1, 0) == 3
    assert Game_of_life.alive_neighbour(matrix, 0, 0) == 2
    assert Game_of_life.alive_neighbour(matrix, 2, 1) == 1
    assert Game_of_life.alive_neighbour(matrix, 2, 2) == 2

def test_for_applying_rules():
    """   1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
   2. Any live cell with two or three live neighbors lives on to the next generation.
   3. Any live cell with more than three live neighbors dies, as if by overpopulation.
   4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""
    matrix=[[0,1,0],
            [0,1,0],
            [0,1,0]]
    assert Game_of_life.apply_rules(matrix,3)==[[0,0,0],[1,1,1,],[0,0,0]]

    matrix=[[0,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,0,0,0]]
    assert Game_of_life.apply_rules(matrix,4)==[[0,0,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]]

    matrix=[[0,1,0],
            [1,1,1],
            [0,1,0]]
    assert Game_of_life.apply_rules(matrix,3)==[[1,1,1],[1,0,1],[1,1,1]]
