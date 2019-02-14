def matrix(number):
    """Returns a 'n x n' matrix, with all element = 0
"""
    matrix=[]
    for i in range(number):
        row=[0]*number
        matrix.append(row)

    return matrix
    
if __name__=='__main__':
    matrix(4)
    
