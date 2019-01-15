import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Returns an array of distances from pacman to the ghosts')
parser.add_argument("--board", help="Path to the file containing the board")
args = parser.parse_args()

if not args.board:
    print("No board path specified")
    exit(-1)

try:
    board = np.load(args.board)
except:
    print("Could not load board")
    exit(-1)

def getPacmanIndex(board):
    temp = np.where(board == 3)
    return (temp[0][0],temp[1][0])

def getGhostIndices(board):
    temp = np.where(board == 2)
    return zip(board[0],board[1])

boardSize = board.shape[0] * board.shape[1]
distancesBoard = (boardSize + 1) * np.ones(board.shape,board.dtype)

def calculateDistances(x,y, currentDistance):
    if x < 0 or x >= board.shape[0]:
        return
    if y < 0 or y >= board.shape[1]:
        return
    if board[x,y] == 1:
        return
    if currentDistance >= distancesBoard[x,y]:
        return
    distancesBoard[x,y] = currentDistance
    calculateDistances(x-1,y,currentDistance + 1)
    calculateDistances(x,y-1,currentDistance + 1)
    calculateDistances(x+1,y,currentDistance + 1)
    calculateDistances(x,y+1,currentDistance + 1)

pacmanIndex = getPacmanIndex(board)
calculateDistances(pacmanIndex[0], pacmanIndex[1], 0)

ghosts = getGhostIndices(board)
print(ghosts)

