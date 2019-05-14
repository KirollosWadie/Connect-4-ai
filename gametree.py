from connect4 import *
from anytree import RenderTree, Node
import numpy as np

def mainpulate_arrays(arr):
    m = np.reshape(arr, (7,7))
    m1 = np.flip(m)
    m2 = np.rot90(m1)
    m3 = m2.astype(int)
    return m3

def gameTree(player, AI, heights):

    z = [] # AI with length 7
    z1 = [] # Player with length 49
    z2 = [] # AI with length 343 
    playerState = Node(player)
    print(player.astype(int))

    # level 1 of the tree
    for i in range (0,7):
        result = make_move(heights[i], AI)
        z.append(Node(result.astype(int), parent=playerState))
        heights[i]+=1

    # level 2
    for j in range(0,7):
        for k in range (0,7):
            result1 = make_move(heights[k], player)
            z1.append(Node(result1.astype(int), parent=z[j]))    
        heights[j]+=1

    # level 3
    arr = np.array(z[0].name)
    for k in range(0,49):
        for l in range (0,7):
            result2 = make_move(heights[l], arr)
            z2.append(Node(result2.astype(int), parent=z1[k]))
            if k == 0:
                heights[l]+=1
            

    print("z",mainpulate_arrays(z[0].name))
    print("z1",mainpulate_arrays(z1[1].name))
    print("z2",mainpulate_arrays(z2[1].name))
    #print(heights)
    return z1

def calc_score(leafs):
    for i in range(0,len(leafs)):
        #print(leafs[i].name)
        pass


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
    heights_copy = np.copy(heights)
    #print(heights_copy)
    player = np.fliplr(player)
    player = player.flatten('F')
    AI = np.fliplr(AI)
    AI = AI.flatten('F')
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
            leafs = gameTree(player, AI, heights)
            calc_score(leafs)
gameLoap()
