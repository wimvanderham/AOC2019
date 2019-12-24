# Day 24 - Planet of Discord - Bugs

import time

start = time.time()

line_counter = 0
row = 0
col = 0
grid = {}
with open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_24.txt") as f:
    # Read input
    for line in f:
        col = 0
        for char in line:
            grid[(row,col)] = char
            col += 1
        row += 1


def calc_biodiversity(calc_grid):
    biodiversity = 0
    power = 1
    for row in range(5):
        for col in range(5):
            if calc_grid[(row,col)] == "#":
                biodiversity += power
            power = power * 2
    return biodiversity

pattern = {}
minute = 0
while True:
    new_grid = {}
    minute += 1
    key = ""
    for row in range(5):
        for col in range(5):
            bugs = 0
            up = (row - 1, col)
            down = (row + 1, col)
            left = (row, col - 1)
            right = (row, col + 1)
            if up in grid and grid[up] == "#":
                bugs += 1
            if down in grid and grid[down] == "#":
                bugs += 1
            if left in grid and grid[left] == "#":
                bugs += 1
            if right in grid and grid[right] == "#":
                bugs += 1
            if grid[(row,col)] == "#":
                # Checks on bug on this position
                if bugs != 1:
                    # Bug dies
                    new_grid[(row,col)] = "."
                else:
                    new_grid[(row,col)] = grid[(row,col)]
            else:
                # Empty space
                if bugs == 1 or bugs == 2:
                    # Empty space comes infected
                    new_grid[(row,col)] = "#"
                else:
                    new_grid[(row,col)] = grid[(row,col)]
            key += new_grid[(row,col)]        
            #print new_grid[(row,col)],
    if key in pattern:
        #print minute, new_grid, "already found in:", pattern[key]
        print "Solution 1:", calc_biodiversity(new_grid)
        break;
    else:
        pattern[key] = minute
    grid = new_grid
        
end = time.time()

print "Found Solution in:", end - start
