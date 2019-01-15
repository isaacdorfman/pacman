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

