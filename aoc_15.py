# Day 15: Oxygen System - Moving a repair droid
#
# The remote control program executes the following steps in a loop forever:
# 
#     Accept a movement command via an input instruction.
#     Send the movement command to the repair droid.
#     Wait for the repair droid to finish the movement operation.
#     Report on the status of the repair droid via an output instruction.

# Only four movement commands are understood: north (1), south (2), west (3), and east (4). Any other command is invalid. The movements differ in direction, but not in distance: in a long enough east-west hallway, a series of commands like 4,4,4,4,3,3,3,3 would leave the repair droid back where it started.

# The repair droid can reply with any of the following status codes:

#     0: The repair droid hit a wall. Its position has not changed.
#     1: The repair droid has moved one step in the requested direction.
#     2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.

import time

program = []

def calc_result(input_parameter_1, input_parameter_2, prog, pos, relative_base):
    
    output_parameter = 0

    which_input = 1

    # Define a dict with the number of parameters for each opcode
    num_parameters = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}
    name_opcode = {1: "add", 2: "mul", 3: "rcv", 4: "snd", 5: "beq", 6: "bne", 7: "slt", 8: "seq", 9: "arb", 99: "hlt"}
    
    while True:
        instruction = prog[pos]
        opcode = instruction % 100
        if opcode == 99:
            break

        instruction = instruction / 100
        parameter_mode = [0, 0, 0]
        parameter_mode[0] = instruction % 10
        instruction = instruction / 10
        parameter_mode[1] = instruction % 10
        instruction = instruction / 10
        parameter_mode[2] = instruction % 10

        if opcode == 1 or opcode == 2:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_out = prog[pos + 3]
            if parameter_mode[0] == 0:
                if reg_in1 < len(prog):
                    operand_1 = prog[reg_in1]
                else:
                    operand_1 = 0
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                if reg_in1 + relative_base < len(prog):
                    operand_1 = prog[reg_in1 + relative_base]
                else:
                    operand_1 = 0
            if parameter_mode[1] == 0:
                if reg_in2 < len(prog):
                    operand_2 = prog[reg_in2]
                else:
                    operand_2 = 0
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                if reg_in2 + relative_base < len(prog):
                    operand_2 = prog[reg_in2 + relative_base]
                else:
                    operand_2 = 0
            if parameter_mode[2] == 2:
                if reg_out + relative_base >= len(prog):
                    while len(prog) <= reg_out + relative_base:
                        prog.append(0)
            else:
                if reg_out >= len(prog):
                    while len(prog) <= reg_out:
                        prog.append(0)

        if opcode == 1:
            result = operand_1 + operand_2
            if parameter_mode[2] == 2:
                prog[reg_out + relative_base] = result
            else:
                prog[reg_out] = result
            pos += 4
        if opcode == 2:
            result = operand_1 * operand_2
            if parameter_mode[2] == 2:
                prog[reg_out + relative_base] = result
            else:
                prog[reg_out] = result
            pos += 4
        if opcode == 3:
            reg_in = prog[pos + 1]
            if which_input == 1:
                if parameter_mode[0] == 0 or parameter_mode[0] == 1:
                    prog[reg_in] = input_parameter_1
                elif parameter_mode[0] == 2:
                    prog[reg_in + relative_base] = input_parameter_1
                which_input = 2
            elif which_input == 2:
                if parameter_mode[0] == 0 or parameter_mode[0] == 1:
                    prog[reg_in] = input_parameter_2
                elif parameter_mode[0] == 2:
                    prog[reg_in + relative_base] = input_parameter_2
                which_input = 3
            else:
                print "Too much input requested"
                raw_input()
            pos += 2
        if opcode == 4:
            reg_out = prog[pos + 1]
            if parameter_mode[0] == 0:
                output_parameter = prog[reg_out]
            elif parameter_mode[0] == 1:
                output_parameter = reg_out
            elif parameter_mode[0] == 2:
                output_parameter = prog[relative_base + reg_out]
            pos += 2
            break
        if opcode == 5:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            
            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
                
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
            if operand_1 <> 0:
                pos = operand_2
            else:
                pos += 3
        if opcode == 6:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
            if operand_1 == 0:
                pos = operand_2
            else:
                pos += 3
        if opcode == 7:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_in3 = prog[pos + 3]
            
            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
                
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
                
            if parameter_mode[2] == 0:
                operand_3 = reg_in3
            elif parameter_mode[2] == 1:
                operand_3 = reg_in3
            elif parameter_mode[2] == 2:
                operand_3 = reg_in3 + relative_base
                
            if operand_1 < operand_2:
                prog[operand_3] = 1
            else:
                prog[operand_3] = 0
            pos += 4
        if opcode == 8:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_in3 = prog[pos + 3]

            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
                
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
                
            if parameter_mode[2] == 0:
                operand_3 = reg_in3
            elif parameter_mode[2] == 1:
                operand_3 = reg_in3
            elif parameter_mode[2] == 2:
                operand_3 = reg_in3 + relative_base
                
            if operand_1 == operand_2:
                prog[operand_3] = 1
            else:
                prog[operand_3] = 0
            pos += 4
        if opcode == 9:
            reg_in1 = prog[pos + 1]
            if parameter_mode[0] == 0:
                relative_base += prog[reg_in1]
            elif parameter_mode[0] == 1:
                relative_base += reg_in1
            elif parameter_mode[0] == 2:
                relative_base += prog[reg_in1 + relative_base]
            pos += 2

        
    return output_parameter, opcode, pos, relative_base


def create_graph(position, distance, P, pos, relative_base):
    x = position[0]
    y = position[1]
    #print "create_graph:", position, distance
    #q = raw_input()
    #if q == "q":
    #    return
    neighbours = []
    for direction in range(1, 5):
        input_1 = direction
        input_2 = ID[direction]

        # New position
        x += Dx[input_1 - 1]
        y += Dy[input_1 - 1]

        next_position = (x,y)

        if next_position in P_grid:
            # Already visited
            if P_grid[next_position] != 0:
                # And not a wall
                neighbours.append(next_position)
        else:
            # Try this new position
            output, opcode, pos, relative_base = calc_result(input_1, 0, P, pos, relative_base)
            #print next_position, output, direction

            if output == 0:
                # Hit the wall
                P_grid[next_position] = 0
                # Position has not changed
            elif output == 1 or output == 2:
                distance += 1
                if output == 2:
                    # Found oxygen system
                    #print "Found oxygen system:", next_position
                    special[2] = next_position
                    print "Found oxygen system at:", next_position, "at:", distance, "steps"
                    # Oxygen system doesn't require fill
                    to_fill[next_position] = False
                    #raw_input()
                else:
                    to_fill[next_position] = True

                # Moved to new position
                P_grid[next_position] = output
                neighbours.append(next_position)

                create_graph(next_position, distance, P, pos, relative_base)
                
                # Move back to prev_position
                output, opcode, pos, relative_base = calc_result(input_2, 0, P, pos, relative_base)
                distance -= 1

        x = position[0]
        y = position[1]
        
    graph[position] = neighbours

def print_maze(min_x, min_y, max_x, max_y):
    nr = 0
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            position = (x,y)
            if position == (0,0):
                line += "*"
                continue
            if position in P_grid:
                status = P_grid[position]
            else:
                status = -1
            if status == -1:
                line += " "
            elif status == 0:
                line += "#"
            elif status == 1:
                line += "."
            elif status == 2:
                line += "O"
            elif status == 3:
                line += "+"
            else:
                nr = status % 10
                line += str(nr)
        print line

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


# ---- MAIN ----
start = time.time()

print "Day 15"
input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_15.txt")
program = [int(x) for x in input_file.read().split(",")]

opcode = 0
pos = 0
relative_base = 0
input_1 = 0
input_2 = 0

P = list(program)
#print P, len(P)

# Dictionary for the grid
P_grid = {}

counter = 0
x = 0
y = 0
min_x = -21
max_x = 19
min_y = -21
max_y = 19
position = (x,y)

D = {1: "north", 2: "south", 3: "west", 4: "east"}
# Inverse direction
ID = {1: 2, 2: 1, 3: 4, 4: 3}

# Change of x coordinate per direction
Dx = [0, 0, -1, +1]
# Change of y coordinate per direction
Dy = [-1, +1, 0, 0]

path = []
direction_path = []

# First step, create a graph
# The graph consists of positions (starting at (0,0)) and neighbours
graph = {}

# Dictionary of open spaces to fill
to_fill = {}

# Dictionary with special locations (starting position and oxygen system)
special = {}

# Initial situation
position = (0,0)
P_grid[position] = 1
special[1] = position
to_fill[position] = True

# Create graph of all positions by recursively calling create_graph
# It will also fill the special dictionary with the location of the oxygen system
# And the to_fill dictionary with the open spaces to fill (for part two)
create_graph(position, 0, P, 0, 0)

print_maze(min_x, min_y, max_x, max_y)

# Now we know the locations, check shortest path using bfs
start_pos = special[1]
goal      = special[2]
print start_pos, goal
 
shortest_path = bfs_shortest_path(graph, (0,0), (16,12))

print shortest_path, len(shortest_path) - 1
for position in shortest_path:
    if position != start_pos and position != goal:
        P_grid[position] = 3

print_maze(min_x, min_y, max_x, max_y)

end = time.time()

print "Found Solution 1 in:", (end - start)
print "Press return to continue part Two...",
raw_input()

# Part 2
start = time.time()

minutes = 0
for position in to_fill.keys():
    shortest_path = bfs_shortest_path(graph, (16,12), position)
    if len(shortest_path) - 1 > minutes:
        minutes = len(shortest_path) - 1
        shortest_shortest_path = list(shortest_path)
        #print shortest_path, minutes

print "Minutes to fill up maze with oxygen:", minutes

position_count = 0
for position in shortest_shortest_path:
    if position != start_pos and position != goal:
        position_count += 1
        P_grid[position] = 1000 + position_count

print_maze(min_x, min_y, max_x, max_y)
end = time.time()

print "Found Solution 2 in:", (end - start)
