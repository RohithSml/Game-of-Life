#Testing file for Game_of_life.py
import Game_of_life


#1.Creating a nxn matrix

def test_4x4_matrix():
    expected_value=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    assert Game_of_life.matrix(4) == expected_value
