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

file = open("input")
input = file.read()

# grid = example.split("\n")
grid = input.split("\n")
for i in range(len(grid)):
    grid[i] = grid[i].rstrip()
width = len(grid[0])
height = len(grid)
print(width)
print(height)
print(grid[0][width -1])
print(grid[height - 1][width - 1])

guardX = 0
guardY = 0
direction = ""
guardChars = "^<>v"
#first figure out where our guard is
for y in range(height):
    print(y)
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

counter = 0
max_count = 10000000
while guardY >= 0 and guardY < height and guardX >= 0 and guardX < width:
    counter += 1
    listedRow = list(grid[guardY])
    if direction == '^':  # UP
        if guardY == 0:
            # exiting grid
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardY -= 1
        elif grid[guardY - 1][guardX] == '.' or grid[guardY - 1][guardX] == 'X':
            # same things happen here as in previous check but let's keep separate because of potential p2
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardY -= 1
        elif grid[guardY - 1][guardX] == '#':
            direction = '>'    
    elif direction == '>':  # RIGHT
        if guardX == width - 1:
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardX += 1
        elif grid[guardY][guardX + 1] == '.' or grid[guardY][guardX + 1] == 'X':
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
        elif grid[guardY + 1][guardX] == '.' or grid[guardY + 1][guardX] == 'X': 
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
        elif grid[guardY][guardX - 1] == '.' or grid[guardY][guardX - 1] == 'X':  
            listedRow[guardX] = 'X'
            grid[guardY] = ''.join(listedRow)
            guardX -= 1
        elif grid[guardY][guardX - 1] == '#':
            direction = '^'
    if counter is max_count:
        break

print_grid()
print(str(count_positions()))
