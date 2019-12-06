import time

start = time.time()

input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_6.txt")

# orbit_map contains the one-way links: if A)B (B is in orbit of A) then orbit_map[B] = A
orbit_map = {}

# orbit graph creates both ways, A - B and B - A
orbit_graph = {}

objects = []

nr_orbit = 0
nr_objects = 0

for orbit in input_file:
    nr_orbit += 1
    a,b = orbit.rstrip().split(")")
    #print nr_orbit, orbit, "a:", a, "b:", b
    orbit_map[b] = a
    if (a in objects) == False:
        objects.append(a)
    if (b in objects) == False:
        objects.append(b)
    if (a in orbit_graph) == False:
        orbit_graph[a] = [b]
    else:
        orbit_graph[a] = orbit_graph[a] + [b]
    if (b in orbit_graph) == False:
        orbit_graph[b] = [a]
    else:
        orbit_graph[b] = orbit_graph[b] + [a]
        
    #orbit_graph[b] = orbit_graph[b].append(a)
        
total_orbits = 0

for object_a in objects:
    object_b = object_a
    while object_b in orbit_map:
        total_orbits += 1
        object_b = orbit_map[object_b]

print "Part 1:", total_orbits

def destinations(start):
    destinations = []
    while start in orbit_map:
        if destinations == []:
            destinations = [start]
        else:
            destinations.append(start)
        start = orbit_map[start]

    return destinations        

dest_You = destinations("YOU")
dest_San = destinations("SAN")

min_distance = 0
for jump in range(1, len(dest_You)):
    jump_to = dest_You[jump]
    if jump_to in dest_San:
        distance = jump + dest_San.index(jump_to)
        if min_distance == 0 or distance < min_distance:
            #print distance, jump_to
            min_distance = distance
        
print "Part 2:", min_distance - 2 # Subtract 2 to correct fact that you don't need to jump to the orbit you're already in
                  
end = time.time()


print "Found Solutions in:", (end - start)





    
