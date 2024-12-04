file = open("input")
contents = file.readlines()
height = len(contents)
# get width when new lines are stripped
# print (contents)
# print(height, width)


# make lines arrays for all directions
left_to_right = contents;
for i in range(height):
    left_to_right[i] = left_to_right[i].rstrip()
# ready to get width
width = len(left_to_right)
# get right to left strings by reversing left to right strings
right_to_left = [0] * height;
for i in range(height):
    right_to_left[i] = ''.join(reversed(left_to_right[i]))
#print(right_to_left)

# up to down columns
top_to_bottom = [0] * width
for x in range(width):
    column = ""
    for y in range(height):
        column += contents[y][x]
    top_to_bottom[x] = column
#print(top_to_bottom)
# down to up columns
bottom_to_top = [0] * width
for i in range(width):
    bottom_to_top[i] = ''.join(reversed(top_to_bottom[i]))
#print(bottom_to_top)

# diagonal columns
bottom_left_to_top_right = []
# start from top left and go round the array (first two sides)
# to catch all diagonal starting points from the edge
boundary_y_inclusive = height - 1
boundary_x_inclusive = width - 1
cur_x = 0
cur_y = 0
start_x = 0
start_y = 0
for starting_point in range(height + width - 1):
    bottom_left_to_top_right.append("")
    
    cur_x = start_x
    cur_y = start_y
    
    while True:
        bottom_left_to_top_right[starting_point] += left_to_right[cur_y][cur_x]  # .join(bottom_left_to_top_right[starting_point])
        cur_y -= 1
        cur_x += 1
        
        if cur_x is width or cur_y == -1:
            # break on first out of bounds
            break;
    
    if start_y < boundary_y_inclusive:
        start_y += 1
    else:
        start_x += 1
        
# print(bottom_left_to_top_right)
# Reversing this is done in counting phase, no need for array
# Next the other way diagonals
bottom_right_to_top_left = []
boundary_y_inclusive = height - 1
boundary_x_inclusive = width - 1
start_x = 0
start_y = boundary_y_inclusive
for starting_point in range(height + width - 1):
    bottom_right_to_top_left.append("")
    
    cur_x = start_x
    cur_y = start_y
    
    while True:
        bottom_right_to_top_left[starting_point] += left_to_right[cur_y][cur_x]  # .join(bottom_left_to_top_right[starting_point])
        cur_y -= 1
        cur_x -= 1
        
        if cur_x == -1 or cur_y == -1:
            # break on first out of bounds
            break;
    
    if start_x < boundary_x_inclusive:
        start_x += 1
    else:
        start_y -= 1


# count all occurrences of XMAS
occurrences = 0
for line in left_to_right:
    occurrences += line.count("XMAS")
for line in right_to_left:
    occurrences += line.count("XMAS")
for line in top_to_bottom:
    occurrences += line.count("XMAS")
for line in bottom_to_top:
    occurrences += line.count("XMAS")
for line in bottom_left_to_top_right:
    occurrences += line.count("XMAS")
    occurrences += ''.join(reversed(line)).count("XMAS")
for line in bottom_right_to_top_left:
    occurrences += line.count("XMAS")
    occurrences += ''.join(reversed(line)).count("XMAS")
print("XMAS found " + str(occurrences) + " times.")

# Part 2
# Here we're finding MASes that are in the shape of an X.
# I got the idea for part 1 that I should do it by finding 
# occurrences of certain letter and looking if the word 
# it continues as it should. I'll do it in here instead.
# So let's find letter A:s and see if it has 2 MAS words
# nearby. :)

occurrences = 0;
wanted_letters = "MS"

for y in range(height):
    if y == 0 or y == height - 1:
        continue
    for x in range(width):
        if x == 0 or x == width -1:
            continue

        if left_to_right[y][x] == 'A':
            top_left = left_to_right[y- 1][x - 1]
            if top_left not in wanted_letters:
                continue
            top_right = left_to_right[y - 1][x + 1]
            if top_right not in wanted_letters:
                continue
            bottom_left = left_to_right[y + 1][x - 1]
            if bottom_left not in wanted_letters:
                continue
            bottom_right = left_to_right[y + 1][x + 1]
            if bottom_right not in wanted_letters:
                continue
            
            if top_left is bottom_right:
                continue
            if top_right is bottom_left:
                continue
            
            occurrences += 1
         
print(str(occurrences))