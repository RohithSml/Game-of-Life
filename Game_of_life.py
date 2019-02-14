def matrix(number):
    """Returns a 'n x n' matrix, with all element = 0
"""
    matrix=[]
    for i in range(number):
        row=[0]*number
        matrix.append(row)

    return matrix
    
def initial(matrix):
    """Creats live cells in the pre-defined nxn  matrix
"""
    matrix[0][1]=1
    matrix[1][1]=1
    matrix[2][1]=1
    
    return matrix

def alive(cell):
    """Checks if the cell is alive;
Returns boolean"""
    if cell==1:
        return True
    else:
        return False

    
