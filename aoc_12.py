# AOC - Day 12 - The N-Body Problem or Moons around Jupiter
# Simulate movement of 4 moons around Jupiter based on 3D position and gravity
# Gravity between moons causes velocity to change
# After that calculate total energy as multiplication of potential and kinetic energy

import time
import numpy as np
import math
import copy

start = time.time()

moons = {}
original = {}

moon = 0
with open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_12_test.txt") as f:
    # Read input of format <x=1, y=2, z=-9> into dictionary
    # with moon number as key and list of 3 coordinates (x, y, z)
    # and 3 velocities (delta_x, delta_y, delta_z) per moon
    for line in f:
        print line
        for axis in line[1:-2].split(", "):
            if axis[0] == "x":
                x_coord = int(axis[2:])
            if axis[0] == "y":
                y_coord = int(axis[2:])
            if axis[0] == "z":
                z_coord = int(axis[2:])
        moons[moon] = [x_coord, y_coord, z_coord, 0, 0, 0]
        original[moon] = [x_coord, y_coord, z_coord, 0, 0, 0]
        moon += 1
    print moons


def total_energy(calc_moon):
    pot = abs(calc_moon[0]) + abs(calc_moon[1]) + abs(calc_moon[2])
    kin = abs(calc_moon[3]) + abs(calc_moon[4]) + abs(calc_moon[5])

    total = pot * kin

    return total

history = {}

for step in range(2773):
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
    history_moons = ""
    for moon in moons.keys():
        from_moon = moons[moon]
        for index in range(3):
            from_moon[index] += from_moon[index + 3]
        history_moons = history_moons + "x[" + str(moon) + "]=" + str(from_moon[0]) + ",y[" + str(moon) + "]=" + str(from_moon[1]) + ",z[" + str(moon) + "]=" + str(from_moon[2]) + "v_x[" + str(moon) + "]=" + str(from_moon[3]) + ",v_y[" + str(moon) + "]=" + str(from_moon[4]) + ",v_z[" + str(moon) + "]=" + str(from_moon[5])
    if history_moons in history:
        print "Found a previous state:", step, history_moons, moons, history[history_moons]
    else:
        history[history_moons] = step
    if step == 999:
        print step, moons
    total = 0
    for moon in moons.keys():
        #print "total:", total_energy(moons[moon]),
        total += total_energy(moons[moon])

    if step == 999:
        print total
    
print "New moons:", moons
print "Original:", original

end = time.time()

print "Found solutions in:", end - start, "seconds"
