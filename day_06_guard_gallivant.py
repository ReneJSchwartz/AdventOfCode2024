example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

grid = example.split("\n")
width = len(grid[0])
height = len(grid)

guardX = 0
guardY = 0
direction = ""
guardChars = "^<>v"
#first figure out where our guard is
for y in range(height):
    for x in range(width):
        if grid[y][x] in guardChars:
            guardX = x
            guardY = y
            direction = grid[y][x]
            listedRow = list(grid[y])
            listedRow[x] = 'X'
            grid[y] = ''.join(listedRow)

print(str(guardY), str(guardX))


def count_positions():
    visitedPositions = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 'X':
                visitedPositions += 1
    return visitedPositions
    
def print_grid():
    print('\n'.join(grid))
    
print_grid()
print()


while guardY >= 0 and guardY < height and guardX >= 0 and guardX < width:
    listedRow = list(grid[guardY])
    if direction == '^':  # UP
        if guardY == 0:
            # exiting grid
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardY -= 1
        elif grid[guardY - 1][guardX] == '.':
            # same things happen here as in previous check but let's keep separate because of potential p2
            guardY -= 1
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
        elif grid[guardY - 1][guardX] == '#':
            direction = '>'    
    elif direction == '>':  # RIGHT
        if guardX == width - 1:
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardX += 1
        elif grid[guardY][guardX + 1] == '.':
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardX += 1
        elif grid[guardY][guardX + 1] == '#':
            direction = 'v'
    elif direction == 'v':  # DOWN
        if guardY == height - 1:
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardY += 1
        elif grid[guardY + 1][guardX] == '.': 
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardY += 1
        elif grid[guardY + 1][guardX] == '#':
            direction = '<'
    elif direction == '<':  # LEFT
        if guardX == 0:
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardX -= 1
        elif grid[guardY][guardX - 1] == '.':  
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardX -= 1
        elif grid[guardY][guardX - 1] == '#':
            direction = '^'

print_grid()
print(str(count_positions()))
