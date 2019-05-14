import numpy as np

def make_move (col, player):
    move = np.zeros((49,))
    index = 48 - col
    move[index] = 1
    result = np.logical_xor(move,player)
    return result


def drawBoard(player):
    print("in draw")
    for row in range(1,7):
        for col in range(0,7):
            if player[row][col] == 1:
                print("|x", end='')
            else:
                print("| ", end='')  
        print("|")       