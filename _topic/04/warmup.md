Minesweeper is a single player game where players reveal spots on an M x N grid, with Z mines.
If they reveal a mine, they lose.  When they reveal a non-mine, the tile is replaced
with the number of adjacent mines, or, if there are no adjacent mines, all adjacent squares are revealed.

They may mark un-revealed spots as mines.  They may then ask a tile to assume those
spots are correct, and (if the number of adjacent mines is satisfied) reveal all other un-revealed adject tiles.

Describe the necessary parts of a program to play Minesweeper.