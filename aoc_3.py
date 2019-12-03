import time

start = time.time()
input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_3.txt")

wire_steps = []
grid = {}
grid_steps = {}
min_distance = 0
min_steps    = 0

deltaX = {"U": 0, "D": 0,  "R": 1, "L": -1}
deltaY = {"U": 1, "D": -1, "R": 0, "L": 0}

for wire in range(1,3):
    print "Wire: ", wire
    wire_path = input_file.readline().rstrip()

    wire_steps = wire_path.split(",")

    x = 0
    y = 0

    step_count = 0
    for step in wire_steps:
        direction = step[0]
        length = int(step[1:])
        #print wire, direction, length

        while length > 0:
            step_count += 1
            y += deltaY[direction]
            x += deltaX[direction]
            
            if (x,y) in grid:
                # Already passed here
                if wire == 2 and grid[(x,y)] == 1:
                    # Both second and first passed here
                    grid[(x,y)] = grid[(x,y)] + wire
                    if grid[(x,y)] == 3:
                        # First time both here
                        grid_steps[(x,y)] = grid_steps[(x,y)] + step_count
                        if min_distance == 0 or (abs(x) + abs(y)) < min_distance:
                            min_distance = abs(x) + abs(y)
                            print "Min distance:", x,y,min_distance
                        if min_steps == 0 or grid_steps[(x,y)] < min_steps:
                            min_steps = grid_steps[(x,y)]
                            print "Min steps:", x, y, min_steps
            else:
                grid[(x,y)] = wire
                grid_steps[(x,y)] = step_count
            length -= 1

end = time.time()

print "Found solution in:", end - start, "seconds"
