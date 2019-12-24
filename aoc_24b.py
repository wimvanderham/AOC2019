# Day 24 - Planet of Discord - Bugs

import time

start = time.time()

line_counter = 0
row = 0
col = 0
# Initial Grid (level 0)
grid = {}
minlevel = -200
maxlevel = 200
# Multigrid (levels from minlevel to maxlevel)
multigrid = {}

with open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_24.txt") as f:
    # Read input
    for line in f:
        col = 0
        for char in line:
            grid[(row,col)] = char
            col += 1
        row += 1

def count_bugs(multigrid, minlevel, maxlevel):
    bugs = 0
    for level in range(minlevel, maxlevel + 1):
        for row in range(5):
            for col in range(5):
                if multigrid[(level,row,col)] == "#":
                    bugs += 1
    return bugs

def init_grid(multigrid, gridlevel):
    for row in range(5):
        for col in range(5):
            if gridlevel == 0:
                # Take value from initial grid
                multigrid[(gridlevel,row,col)] = grid[(row,col)]
            else:
                # Start with empty space
                multigrid[(gridlevel,row,col)] = "."
    
def get_new_multigrid(multigrid_in):
    multigrid_out = {}
    for gridlevel in range(minlevel, maxlevel + 1):
        for row in range(5):
            for col in range(5):
                bugs = 0
                if row == 2 and col == 2:
                    multigrid_out[(gridlevel, row, col)] = "."
                    continue
                if row == 0:
                    # On Top row, check level - 1
                    up = (gridlevel - 1, 1, 2)
                else:
                    up = (gridlevel, row - 1, col)
                if row == 4:
                    # On Bottom row, check level - 1
                    down = (gridlevel - 1, 3, 2)
                else:                
                    down = (gridlevel, row + 1, col)
                if col == 0:
                    # On first Column, check level - 1
                    left = (gridlevel - 1, 2, 1)
                else:
                    left = (gridlevel, row, col - 1)
                if col == 4:
                    # On Last Column, check level - 1
                    right = (gridlevel - 1, 2, 3)
                else:
                    right = (gridlevel, row, col + 1)
                if up in multigrid_in and multigrid[up] == "#":
                    bugs += 1
                if down in multigrid_in and multigrid[down] == "#":
                    bugs += 1
                if left in multigrid_in and multigrid[left] == "#":
                    bugs += 1
                if right in multigrid_in and multigrid[right] == "#":
                    bugs += 1
                if row == 3 and col == 2:
                    # Special case, check next level + 1
                    # Check bugs up on next level
                    up_level = (gridlevel + 1, 4, 0)
                    if up_level in multigrid_in:
                        for up_col in range(5):
                            # Check all grids up level can reach
                            if multigrid_in[(gridlevel + 1, 4, up_col)] == "#":
                                bugs += 1
                if row == 1 and col == 2:
                    # Check bugs down on next level
                    down_level = (gridlevel + 1, 0, 0)
                    if down_level in multigrid_in:
                        for down_col in range(5):
                            # Check all grids down level can reach
                            if multigrid_in[(gridlevel + 1, 0, down_col)] == "#":
                                bugs += 1
                if row == 2 and col == 3:
                    # Check bugs left on next level
                    left_level = (gridlevel + 1, 0, 4)
                    if left_level in multigrid_in:
                        for left_row in range(5):
                            # Check all grids left level can reach
                            if multigrid_in[(gridlevel + 1, left_row, 4)] == "#":
                                bugs += 1
                if row == 2 and col == 1:
                    # Check bugs right on next level
                    right_level = (gridlevel + 1, 0, 0)
                    if right_level in multigrid_in:
                        for right_row in range(5):
                            # Check all grids right level can reach
                            if multigrid_in[(gridlevel + 1, right_row, 0)] == "#":
                                bugs += 1
                #print gridlevel, row, col
                if multigrid_in[(gridlevel,row,col)] == "#":
                    # Checks on bug on this position
                    if bugs != 1:
                        # Bug dies
                        multigrid_out[(gridlevel,row,col)] = "."
                    else:
                        multigrid_out[(gridlevel,row,col)] = multigrid_in[(gridlevel,row,col)]
                else:
                    # Empty space
                    if bugs == 1 or bugs == 2:
                        # Empty space comes infected
                        multigrid_out[(gridlevel,row,col)] = "#"
                    else:
                        multigrid_out[(gridlevel,row,col)] = multigrid_in[(gridlevel,row,col)]
    return multigrid_out

# Init multi level grid
for level in range(minlevel, maxlevel + 1):
    #print "Init multigrid:", level
    init_grid(multigrid, level)
    #print multigrid

minute = 0
while True:

    minute += 1
    multigrid = get_new_multigrid(multigrid)
    if minute == 200:
        total_bugs = 0
        for level in range(minlevel, maxlevel + 1):
            #print "Depth:", level
            sub_total = 0
            for row in range(5):
                line = ""
                for col in range(5):
                    line += multigrid[(level, row, col)]
                    if multigrid[(level, row, col)] == "#":
                        sub_total += 1
                #print line
            #print sub_total
            total_bugs += sub_total
            #print
        print "Solution 2:", count_bugs(multigrid, minlevel, maxlevel), total_bugs
        break
    
end = time.time()

print "Found Solution in:", end - start
