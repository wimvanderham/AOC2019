# Day 20 -  Donut Maze - Maze with jumps
import time

grid = {}
maxrow = 0
maxcol = 0
jump_dict = {}
connections = {}

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

def create_grid(f):
    # Read input from file
    maxrow = 0
    maxcol = 0
    row = 0
    for line in f:
        col = 0
        for char in line.rstrip():
            grid[(row,col)] = char
            col += 1
            if maxcol == 0 or col > maxcol:
                maxcol = col
        row += 1
        if maxrow == 0 or row > maxrow:
            maxrow = row
    return maxrow, maxcol

def create_jump_dict(grid):
    # Find "special" places to jump to
    for place in grid.keys():
        char = grid[place]
        if char not in ["#", ".", " "]:
            # Special character, look for "partner"
            #print place, char
            down = (place[0] + 1, place[1])
            if down in grid and grid[down] not in ['#', '.', ' ']:
                # Found "partner"
                jump = char + grid[down]
                gate = (place[0] + 2, place[1])
                if gate in grid and grid[gate] == ".":
                    point = gate
                else:
                    gate = (place[0] - 1, place[1])
                    if gate in grid and grid[gate] == ".":
                        point = gate
                if jump not in jump_dict:
                    jump_dict[jump] = point
                else:
                    jump_dict[jump] = [jump_dict[jump], point]
                #print jump_dict
            else:
                right = (place[0], place[1] + 1)
                if right in grid and grid[right] not in ['#', '.', ' ']:
                    # Found partner to the right
                    jump = char + grid[right]
                    gate = (place[0], place[1] + 2)
                    if gate in grid and grid[gate] == ".":
                        point = gate
                    else:
                        gate = (place[0], place[1] - 1)
                        if gate in grid and grid[gate] == ".":
                            point = gate
                    if jump not in jump_dict:
                        jump_dict[jump] = point
                    else:
                        jump_dict[jump] = [jump_dict[jump], point]
                    #print "right:", jump, jump_dict

def create_connections(jump_dict):
    connections = {}
    for jump in jump_dict:
        #print jump, jump_dict[jump]
        jump_list = jump_dict[jump]
        if jump == 'AA':
            start_position = jump_list
        elif jump == 'ZZ':
            end_position = jump_list
        else:
            connections[jump_list[0]] = jump_list[1]
            connections[jump_list[1]] = jump_list[0]
    return connections, start_position, end_position

def create_graph(grid, connections):
    # Create graph from grid and connections
    x = 0
    y = 0
    Dx = [0, 0, -1, +1]
    Dy = [-1, +1, 0, 0]
    graph = {}
    for position in grid.keys():
        neighbours = []
        if position in connections:
            neighbours.append(connections[position])
            #print position, neighbours
        x = position[0]
        y = position[1]
        for direction in range(4):
            new_x = x + Dx[direction]
            new_y = y + Dy[direction]
            new_position = (new_x, new_y)
            if new_position in grid and grid[new_position] == ".":
                neighbours.append(new_position)
        if len(neighbours) > 0:
            graph[position] = neighbours
            #print position, neighbours
    return graph

def print_grid(grid, maxrow, maxcol):
    footer = ""
    line = "    "
    for col in range(maxcol):
        line += str(int(col / 100) % 10)
    print
    print line
    footer = line
    line = "    "
    for col in range(maxcol):
        line += str(int(col / 10) % 10)
    print line
    footer = line + "\n" + footer
    line = "    "
    for col in range(maxcol):
        line += str(col % 10)
    print line
    footer= line + "\n" + footer
    print
    # Print grid with path from start_position to end_position
    for row in range(maxrow):
        line = '{:3d}'.format(row) + " "
        for col in range(maxcol):
            position = (row, col)
            if position in grid:
                line += str(grid[position])
            else:
                line += " "
        line += " " + str(row)
        print line
    print
    print footer
    print
    
# -- MAIN
start = time.time()

f = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_20.txt")
maxrow, maxcol = create_grid(f)
create_jump_dict(grid)
connections, start_position, end_position = create_connections(jump_dict)
graph = create_graph(grid, connections)

#for position in connections:
#    print position, connections[position]

print "Find path from:", start_position, "to:", end_position

# Now find shortest path
shortest_path = bfs_shortest_path(graph, start_position, end_position)

# Indicate steps on the grid
step = 0
for position in shortest_path:
    grid[position] = step % 10
    if position != end_position:
        step += 1

print_grid(grid, maxrow, maxcol)
        
print "Solution 1:", step, "steps"

end = time.time()

print "Found solution in:", end - start, "seconds"
