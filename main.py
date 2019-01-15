import argparse
import numpy as np

def loadBoard():
    parser = argparse.ArgumentParser(description='Returns an array of distances from pacman to the ghosts')
    parser.add_argument("--board", help="Path to the file containing the board")
    args = parser.parse_args()

    if not args.board:
        print("No board path specified")
        exit(-1)

    try:
        return np.load(args.board)
    except:
        print("Could not load board")
        exit(-1)

def getPacmanIndex(board):
    temp = np.where(board == 3)
    return (temp[0][0],temp[1][0])

def getGhostIndices(board):
    temp = np.where(board == 2)
    return zip(temp[0],temp[1])

def calculateDistances(board, distancesBoard, x,y, currentDistance):
    if x < 0 or x >= board.shape[0]:
        return
    if y < 0 or y >= board.shape[1]:
        return
    if board[x,y] == 1:
        return
    if currentDistance >= distancesBoard[x,y]:
        return
    distancesBoard[x,y] = currentDistance
    calculateDistances(board, distancesBoard, x-1, y, currentDistance + 1)
    calculateDistances(board, distancesBoard, x, y-1, currentDistance + 1)
    calculateDistances(board, distancesBoard, x+1, y, currentDistance + 1)
    calculateDistances(board, distancesBoard, x, y+1, currentDistance + 1)

board = loadBoard()
boardMaxDistance = board.shape[0] + board.shape[1]
#A matrix with the shape of the board where each cell's value is larger than the maximum possible distance in the board
distancesBoard = boardMaxDistance * np.ones(board.shape,board.dtype)

pacmanIndex = getPacmanIndex(board)
calculateDistances(board, distancesBoard, pacmanIndex[0], pacmanIndex[1], 0)

ghosts = getGhostIndices(board)
ghosts.sort(key=lambda x: distancesBoard[x])

print [[idx, distancesBoard[idx]] for idx in ghosts]

