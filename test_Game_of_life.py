#Testing file for Game_of_life.py
import Game_of_life


#1.Creating a nxn matrix

def test_3x3_matrix():
    expected_value=[[0,0,0],[0,0,0],[0,0,0]]
    assert Game_of_life.matrix(3) == expected_value

def test_initializing_predefined_live_cells():
    matrix=[[0,1,0],[0,0,0],[0,0,0]]
    expected_value= [[0,1,0],[0,1,0],[0,1,0]]
    assert Game_of_life.initial(matrix)== matrix
    
def test_for_cell_alive():
    matrix=[[0,1,0],[0,1,0],[0,1,0]]
    assert Game_of_life.alive(matrix[0][1])==1
    assert Game_of_life.alive(matrix[1][1])==1
    assert Game_of_life.alive(matrix[2][1])==1

def test_for_killing_cell():
    matrix=[[1,1,0],[0,0,1],[0,0,1]]
    Game_of_life.die(matrix, 0, 1)
    assert matrix == [[1,0,0],[0,0,1],[0,0,1]]
    Game_of_life.die(matrix, 0, 0)
    assert matrix == [[0,0,0],[0,0,1],[0,0,1]]
    Game_of_life.die(matrix, 0, 2)
    assert matrix == [[0,0,0],[0,0,1],[0,0,1]]
