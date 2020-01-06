# Day 18:  - Finding the keys
#

import time


# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("

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

Dx = [0, 0, +1, -1]
Dy = [+1, -1, 0, 0]
def create_graph(start, max_x, max_y):
    x = start[0]
    y = start[1]

    if x == 40 and y == 41:
        debug = True
    else:
        debug = False
    debug = False

    if debug:
        print start
        
    if x > max_x or y > max_y:
        # Position outside of grid
        if debug:
            print "x or y too big", x, max_x, y, max_y
        return
    if x < 0 or y < 0:
        if debug:
            print "x or y too little", x, y
        return

    neighbours = []
    # Add this position to the graph to exclude recursive call
    graph[start] = neighbours
    if debug:
        print start, graph[start], neighbours
    
    for direction in range(4):
        # Look in 4 directions
        new_pos = (x + Dx[direction], y + Dy[direction])
        if debug:
            print direction, new_pos            
        if new_pos in grid:
            if debug:
                print "new pos in grid:", new_pos, grid[new_pos]
            grid_pos = grid[new_pos]
            if grid_pos in keys or grid_pos in doors or grid_pos == "@":
                if debug:
                    print "new pos in keys or @:", new_pos, grid_pos
                    if grid_pos in keys:
                        print keys[grid_pos]
                neighbours.append(new_pos)
                if new_pos not in graph:
                    create_graph(new_pos, max_x, max_y)
        else:
            neighbours.append(new_pos)
            if new_pos not in graph:
                create_graph(new_pos, max_x, max_y)

    graph[start] = neighbours

def get_doors(path, doors):
    door_list = []
    for position in path:
        if position in grid:
            door = grid[position]
            if door in doors:
                door_list.append(door)
    return door_list
                
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
max_x = 0
max_y = 0

for inputline in input_file.readlines():
    x = 0
    for char in inputline.rstrip():
        if char != ".":
            # Only keep track of "closed" spaces
            position = (x,y)
            grid[position] = char
            if ord(char) >= ord("a") and ord(char) <= ord("z"):
                keys[char] = position
            elif ord(char) >= ord("A") and ord(char) <= ord("Z"):
                doors[char] = position
            elif char == "@":
                start_position = position
        x += 1
        if x > max_x:
            max_x = x
    y += 1
    if y > max_y:
        max_y = y


#print_grid(max_x, max_y)
print "Keys:", keys
print "Doors:", doors
print "Start position:", start_position, grid[start_position]

create_graph(start_position, max_x, max_y)
#print graph

key_pick_list = []
total_steps = 0
find_keys = dict(keys)
closed_doors = dict(doors)

while find_keys:
    # While there are keys to find    
    shortest = -1
    possible_keys = []
    for key in sorted(find_keys.keys()):
        shortest_path = bfs_shortest_path(graph, start_position, find_keys[key])
        if shortest_path != "So sorry, but a connecting path doesn't exist :(":
            # Remove start position from the path (to get "real" steps)
            shortest_path.pop(0)
            # Check for closed doors on our path
            door_list = get_doors(shortest_path, closed_doors)
            print key, start_position, keys[key], len(shortest_path), door_list
            if door_list == []:
                # No closed doors on my path, keep track of shortest shortest_path
                possible_keys.append(key)
                if shortest == -1 or len(shortest_path) < shortest:
                    shortest_shortest_path = list(shortest_path)
                    shortest = len(shortest_path)
        else:
            print key, start_position, keys[key], "No path"


    print "Found shortest path in:", shortest, "steps:", shortest_shortest_path, 
    destination = shortest_shortest_path[-1]
    key = grid[destination]
    print "To destination:", destination, "with key:", key
    if len(possible_keys) == 1:
        key = possible_keys[0]
    else:
        print "Give key to take of possible keys:", possible_keys,
        input_key = raw_input()
        if input_key in possible_keys:
            key = input_key
    shortest_shortest_path = bfs_shortest_path(graph, start_position, find_keys[key])
    shortest_shortest_path.pop(0)
    print "Found shortest_path from:", start_position, "to:", find_keys[key], key, ":", shortest_path
    # Of all possible keys to pick, I choose the closest one
    destination = shortest_shortest_path[-1]
    key = grid[destination]
    key_pick_list.append(key)
    total_steps += len(shortest_shortest_path)
    # Remove the found key from the list of keys to find
    find_keys.pop(key, None)
    # Set the key position as the new start_position
    start_position = destination
    door = key.upper()
    if door in closed_doors:
        closed_doors.pop(door, None)
    print "Next run, from:", start_position, "key:", key, "remaining closed doors:", closed_doors, "keys left to find:", len(find_keys)

print "Key list:", key_pick_list
print "Total steps:", total_steps

end = time.time()

print "Found Solution 1 in:", (end - start)
print "Press return to continue part Two...",
raw_input()

# Part 2
start = time.time()


end = time.time()
print "Found Solution 2 in:", (end - start)
