import argparse

parser = argparse.ArgumentParser(description='Returns an array of distances from pacman to the ghosts')
parser.add_argument("--board", help="Path to the file containing the board")
args = parser.parse_args()

if not args.board:
    print("No board path specified")
    exit(-1)
