# Day 18:  - Finding the keys
#

import time
import collections
from collections import namedtuple
from collections import deque

def print_grid(max_x, max_y):
    for y in range(max_y):
        line = ""
        for x in range(max_x):
            position = (x,y)
            if position in grid:
                char = grid[position]
            else:   
                char = "."
            line += char
        print line
                
# ---- MAIN ----
start = time.time()

print "Day 18"
input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_18.txt")

grid = {}
keys = {}
doors = {}
graph = {}

x = 0
y = 0
Dx = [0, 0, +1, -1]
Dy = [+1, -1, 0, 0]

for inputline in input_file.readlines():
    x = 0
    for char in inputline.rstrip():
        position = (x,y)
        grid[position] = char
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            # A key
            keys[char] = position
        elif ord(char) >= ord("A") and ord(char) <= ord("Z"):
            # A door
            doors[char] = position
        elif char == "@":
            # Start position
            start_position = position
        x += 1
    y += 1

max_position = max(grid)
max_x = max_position[0] + 1
max_y = max_position[1] + 1

# Print input grid
#print_grid(max_x, max_y)

#print "Keys:", keys
#print "Doors:", doors
#print "Start position:", start_position, grid[start_position]
#print "Grid:", grid

# Keep track of position AND keys and distance
State = namedtuple('State', ['x', 'y', 'keys', 'd'])

x = start_position[0]
y = start_position[1]
Q = deque() 
Q.append(State(x, y, set(), 0))

counter = 0
SEEN = set()
while Q:
    S = Q.popleft()
    counter += 1
    key = (S.x, S.y, tuple(sorted(S.keys)))
    if key in SEEN:
        # Already been here with the same keys
        continue
    SEEN.add(key)
    position = (S.x, S.y)
    if position not in grid:
        # Probably won't happen (we've got a surrounding wall)
        print "Strange this happened at position:", position,
        raw_input ("\nPress return to continue.")
        continue
    if grid[position] == "#":
        # This should probably not happen either because I checked it before
        print "Finding a wall on the queue:", position
        raw_input ("\nPress return to continue.")
        continue
    newkeys = set(S.keys)
    position = (S.x, S.y)
    #print counter,
    #print "Checking position:", position, "with keys:", newkeys

    if grid[position] >= 'a' and grid[position] <= 'z':
        # A Key, pick it up
        newkeys.add(grid[position])
        #print counter, "Found key:", grid[position], "at position:", position, newkeys, len(newkeys)
        #raw_input ("\nPress return to continue.")
        #S.keys.add(grid[position])
        #print S.x, S.y, S.keys, newkeys, S.d
        if len(newkeys) == len(keys):
            print "Found all keys in:", S.d, "steps"
            print S.x, S.y, S.keys, S.d
            break

    if grid[position] >= 'A' and grid[position] <= 'Z':
        # A door, check for the key
        #print "A door:", grid[position], "I've got keys:", newkeys
        #print position, grid[position], newkeys
        if grid[position].lower() not in newkeys:
            #print "I can not pass"
            continue

    # Look for neighbours    
    for direction in range(4):
        new_x = S.x + Dx[direction]
        new_y = S.y + Dy[direction]
        new_position = (new_x, new_y)
        if grid[new_position] != "#":
            Q.append(State(new_x, new_y, newkeys, S.d + 1))
        
end = time.time()

print "Found Solution 1 in:", (end - start)
