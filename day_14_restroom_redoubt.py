""" Day 14: Restroom Redoubt

Calculates where robots are after 100 seconds. The robots move in a grid 
and teleport to the other side when they reach grid edges.
"""
import re
import math

input = open("input").read().split("\n")
room_size_x = 11 - 1
room_size_y = 7 - 1

seconds_to_count = 100

# end goal is to see how many robots are in grid quadrants
quadrants = [0, 0, 0, 0]

for robot in input:
    x_start, y_start, x_velocity, y_velocity = re.findall(r'\d+', robot)
    x_start = int(x_start)
    y_start = int(y_start)
    x_velocity = int(x_velocity)
    y_velocity = int(y_velocity)
    v_pos = robot.index('v')
    second_comma_pos = [pos for pos, char in enumerate(robot) if char == ','][1]
    if robot[v_pos + 1] == '-':
        x_velocity = x_velocity * -1
    if robot[second_comma_pos + 1] == '-':
        y_velocity = y_velocity * -1
        
    end_x = x_start + seconds_to_count * x_velocity
    end_y = y_start + seconds_to_count * y_velocity

    # there's a bug in some of the examples but p=2,4 v=2,-3 works
    end_x = end_x % (room_size_x + 1)
    end_y = end_y % (room_size_y + 1)
    
    # assign to a quadrant
    half_x = int(room_size_x / 2)
    half_y = int(room_size_y / 2)
    if end_x < half_x and end_y < half_y:
        quadrants[0] += 1
        print(f"{end_x}, {end_y}")
    elif end_x > half_x and end_y < half_y:
        quadrants[1] += 1
    elif end_x < half_x and end_y > half_y:
        quadrants[2] += 1
    elif end_x > half_x and end_y > half_y:
        quadrants[3] += 1

    print('start pos: ' + str(x_start) + ',' + str(y_start) + ', end pos: ' + str(end_x) + ',' + str(end_y))
    
print(math.prod(quadrants))
