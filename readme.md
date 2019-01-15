# Methods:

- loadBoard: Parses the command line arguments to check if --board <pathToBoard> exists, and if so tries to load the board from that path. If argument does not exist or can't load the board, prints message and exits.

- getPacmanIndex(board): Returns a length 2 tuple containing the index of pacman in the board.

- getGhostIndices(board): Return an array of length 2 tuples, each containing the index of a ghost in the board.

- calculateDistances(board, distancesBoard, x,y, currentDistance): Gets the board, a MUTABLE matrix containing the currently calculated distances in the board which is initialized so that each cell's value is higher than the max possible value, the indices of the current step, and the current depth of recursion.

  Recursion stops when reaching out of bounds, getting into a wall, or having currentDistance greater or equal to the value of the current cell.

  Updates the distancesBoard so that each of it's cells represent the distance of the cell from pacman.