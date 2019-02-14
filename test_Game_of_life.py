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
    
