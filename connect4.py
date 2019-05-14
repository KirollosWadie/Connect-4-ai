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


def gameLoap():
    # Encoding bitBoards to be like:
    # col6 .... col3 col2 col1 col0
    # Example if col 0 =
    # 1
    # 0
    # 0
    # After encoding: 100
    x = input("Choose 'x' or 'o' ")
    player = np.zeros((7,7), dtype=int)
    AI = np.zeros((7,7), dtype=int)
    # To be filled
    heights = np.array([0,7,14,21,28,35,42])
    player = np.fliplr(player)
    player = player.flatten('F')
    if x == 'x':
        while True:
            colNum = input("Enter Col: ")
            z = heights[int(colNum)]
            player = make_move(z, player)
            heights[int(colNum)]+=1 
            # reshape player again to its original
            m = np.reshape(player, (7,7))
            m1 = np.flip(m)
            m2 = np.rot90(m1)
            m3 = m2.astype(int)
            drawBoard(m3)
            print('AI turns')
if __name__ == "__main__":
    gameLoap()