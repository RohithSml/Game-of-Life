def matrix(number):
    """Returns a 'n x n' matrix, with all element = 0"""
    matrix=[]
    for i in range(number):
        row=[0]*number
        matrix.append(row)
    return matrix

def initial(matrix):
    """Creats live cells in the pre-defined nxn  matrix"""
    # Try to make your matrix  immutable
    ret = matrix[:]
    ret[0][1]=1
    ret[1][1]=1
    ret[2][1]=1
    return ret

def alive(cell):
    """Checks if the cell is alive, Returns boolean"""
    return cell == 1 # The if is unnecessary.
    
def die(current, row, col):
    """Kills the cell i.e funtion changes cell's value to 0 and updates
matrix""" # Use a variable name which shows how the parameters are independent of who's calling this function
    ret=current[:]
    ret[row][col]=0
    return ret
def live(matrix, row, col):
    """Creates life in the cell i.e function changes cell's value to 1 and updates matrix"""
    ret=matrix[:]
    ret[row][col]=1
    return ret

def alive_neighbour(first_position, row, col):
    """Returns the number of neighbouring cells that are alive"""
    size_limit = len(first_position)-1
    alive_mem = 0
    for row_probability in [-1, 0, 1]: # Loop variables are usually small
        for col_probability in [-1, 0, 1]:
            next_row = row + row_probability
            next_col = col + col_probability
            if next_row == row and next_col == col:
                continue
            if next_row < 0 or next_col < 0 or next_row > size_limit or next_col > size_limit:
                continue
            if alive(first_position[next_row][next_col]):
                alive_mem = alive_mem+1
    return alive_mem

def apply_rules(current_gen,size):
    """  Applies rules of conway's game of life,and Returns the updated matrix  ."""
    next_gen=matrix(size)

    for i in range (size):
        for j in range (size):
            if alive(current_gen[i][j]) and alive_neighbour(current_gen,i,j) in [2,3]:
                next_gen = live(next_gen,i,j)

            if not alive(current_gen[i][j]) and alive_neighbour(current_gen,i,j) == 3:
                next_gen = live(next_gen,i,j)

            if alive(current_gen[i][j]) and alive_neighbour(current_gen,i,j) < 2:
               next_gen = die(next_gen,i,j)

            if alive(current_gen[i][j]) and alive_neighbour(current_gen,i,j) > 3:
                next_gen=die(next_gen,i,j)

    return next_gen


def display(count,size,first_position):
    """Displays the Matrix in a formatted fashion """
    print("Gen {}\n".format(count))
    for i in range(size):
        for j in range(size):
            print("{:4}".format(first_position[i][j]),end=' ')
        print("\n")

def main():
    """Runs Conway's Game of Life in an infinte loop """
    size=3
    current_gen=initial(matrix(size))
    count =0
    
    try:
        while True:
            display(count,size,current_gen)
            time.sleep(1)
            current_gen=apply_rules(current_gen,size)
            count+=1
    except KeyboardInterrupt:
        print("Interrupted")
                        
if __name__=='__main__':
    import time
    main()
