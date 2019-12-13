# AOC - Day 12 - The N-Body Problem or Moons around Jupiter
# Simulate movement of 4 moons around Jupiter based on 3D position and gravity
# Gravity between moons causes velocity to change
# After that calculate total energy as multiplication of potential and kinetic energy

import time
import numpy as np
import math

start = time.time()

moons = {}
original = {}

# Sort of legend for the moons dictionary
axis_name = {0: "x", 1: "y", 2: "z", 3: "v_x", 4: "v_y", 5: "v_z"}

moon = 0
with open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_12.txt") as f:
    # Read input of format <x=1, y=2, z=-9> into dictionary
    # with moon number as key and list of:
    # 3 coordinates (x, y, z) and
    # 3 velocities (v_x, v_y, v_z) per moon
    for line in f:
        #print line
        for axis in line[1:-2].split(", "):
            if axis[0] == "x":
                x_coord = int(axis[2:])
            if axis[0] == "y":
                y_coord = int(axis[2:])
            if axis[0] == "z":
                z_coord = int(axis[2:])
        moons[moon] = [x_coord, y_coord, z_coord, 0, 0, 0]
        # Save staring position in original dictionary for comparison
        original[moon] = [x_coord, y_coord, z_coord, 0, 0, 0]
        moon += 1
    print "Starting situation:", moons

def total_energy(calc_moon):
    pot = abs(calc_moon[0]) + abs(calc_moon[1]) + abs(calc_moon[2])
    kin = abs(calc_moon[3]) + abs(calc_moon[4]) + abs(calc_moon[5])

    total = pot * kin

    return total

# Keep history of position and velocity per axis for all moons
history = {}
axis_list = []
cycle_list = []
step = 0

# Store starting position in history by axis
for index in range(3):
    # Loop through coordinates and velocities
    history_moons = ""
    for moon in moons.keys():
        # For every moon, construct axis info as character key
        from_moon = moons[moon]
        if history_moons <> "":
            history_moons = history_moons + ", "
        else:
            history_moons = axis_name[index] + ": ["
        history_moons = history_moons  + str(from_moon[index]) + ", " + str(from_moon[index + 3])
    history_moons = history_moons + "]"
    # Example of key values of original situation:
    # axis: [moon[0]_axis, moon[0]_velocity, moon[1]_axis, moon[1]_velocity, moon[2]_axis, moon[2]_velocity]
    # x: [-1, 0, 2, 0, 4, 0, 3, 0]
    # y: [0, 0, -10, 0, -8, 0, 5, 0]
    # z: [2, 0, -7, 0, 8, 0, -1, 0]
    #print moons
    #print step, history_moons
    history[history_moons] = step

found = False
while found == False:
    # Calculate velocity based on gravity
    for moon in moons.keys():
        from_moon = moons[moon]
        for other in moons.keys():
            if other == moon:
                continue
            to_moon = moons[other]

            #print "Compare:", moon, from_moon, "to:", other, to_moon,
            for index in range(3):
                if to_moon[index] > from_moon[index]:
                    from_moon[index + 3] += 1
                if to_moon[index] < from_moon[index]:
                    from_moon[index + 3] += -1
            #print "Result:", from_moon
    # Apply new positions
    for moon in moons.keys():
        from_moon = moons[moon]
        history_moons = ""
        for index in range(3):
            from_moon[index] += from_moon[index + 3]

    # Store history by axis
    for index in range(3):
        # Loop through coordinates and velocities
        history_moons = ""
        for moon in moons.keys():
            # For every moon, construct axis info
            from_moon = moons[moon]
            if history_moons <> "":
                history_moons = history_moons + ", "
            else:
                history_moons = axis_name[index] + ": ["
            history_moons = history_moons  + str(from_moon[index]) + ", " + str(from_moon[index + 3])
        history_moons = history_moons + "]"
        #print moons
        #print step, history_moons
        if history_moons in history:
            #print "Found a previous state for:", axis_name[index], "at:", step, history_moons, moons, history[history_moons]
            if (axis_name[index] in axis_list) == False:
                # First time for this axis
                if axis_list == []:
                    # First axis found
                    print "Solution 2:"
                    print "Axis cycle at:"
                axis_list.append(axis_name[index])
                cycle_list.append(step + 1)
                print axis_name[index], step
                #print history[history_moons], step - history[history_moons], cycle_list
            if len(axis_list) == 3:
                print "Found all cycles!",
                print cycle_list
                found = True
        else:
            history[history_moons] = step

    if step == 999:
        # Solution to the first part
        print "Solution 1:", step, moons
        total = 0
        for moon in moons.keys():
            #print "total:", total_energy(moons[moon]),
            total += total_energy(moons[moon])
        print total
        
    step += 1
#    if step % 10000 == 0:
#        print step, time.time()


print "Now calculate the LCM of:", cycle_list

# Python program to find the L.C.M. of two input number
# This function computes GCD 
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm


print "The LCM is", compute_lcm(cycle_list[0], compute_lcm(cycle_list[1], cycle_list[2]))
#print "https://www.calculatorsoup.com/calculators/math/lcm.php?input=" + str(cycle_list[0]) + "+" + str(cycle_list[1]) + "+" + str(cycle_list[2]) + "&data=none&action=solve"
    
end = time.time()

print "Found solutions in:", end - start, "seconds"
