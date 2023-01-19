from scipy.ndimage import convolve
from matplotlib import pyplot
import numpy as np
game_board = np.zeros((7,7),np.int8)
game_board[:3,:3] = [[0,1,0],[0,0,1],[1,1,1]]
pyplot.imshow(game_board,cmap="binary")

neighbor_kernel = np.ones((3,3))
neighbor_kernel[1,1] = 0

def life_step(game_board):
    neighbor_sums = convolve(game_board,neighbor_kernel,mode="wrap")

    # If fewer than 2 neighbors, cell is dead.
    game_board[neighbor_sums < 2] = 0
    # If 2 neighbors, cell stays in its state.
    # If 3 neighbors, cell becomes or stays active.
    game_board[neighbor_sums == 3] = 1
    # If >3 neighbors, cell dies
    game_board[neighbor_sums > 3] = 0

life_step(game_board)
pyplot.imshow(game_board,cmap="binary")
pyplot.show()
