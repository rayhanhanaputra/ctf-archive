import pwn as p

conn = p.remote("192.168.125.100",9003)

conn.recvuntil(b'Ready? (Y/N)')
conn.sendline("Y")

# Getting and parsing the labyrinth by removing spaces & splitting into a matrix
lab = list(map(lambda x: list(x),conn.recvuntil("\n\n").decode().strip().replace(" ","").split("\n")))

# A very complex way of replacing everything in the matrix
lab = list(map(lambda x: list(map(lambda y: int(y.replace("#", "0").replace("O", "1").replace("L", "1").replace("H", "1")), x)),lab))

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

grid = Grid(matrix=lab)

start = grid.node(0, 0) # Where L was
end = grid.node(len(lab) - 1, len(lab[len(lab) - 1]) - 1) # Where H was
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

last = path[0]
directions = {(0, 1): "D", (0, -1): "U", (1, 0): "R", (-1, 0): "L"} # A dict that replaces multiple if statements
log = ""
for i in path:
    if last == i: # Ignoring the first run
        continue

    log += directions[tuple(map(lambda a, b: a - b, i, last))] # Subtracting two tuples
    last = i

conn.sendline(log) # Sending the directions
print(conn.recvall().decode()) # Prints the flag and the rest of the response   