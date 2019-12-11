# AOC - Day 10 - Asteroids monitoring
# Your job is to figure out which asteroid would be the best place to build a new monitoring station. A monitoring station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid exactly between them. This line of sight can be at any angle, not just lines aligned to the grid or diagonally. The best location is the asteroid that can detect the largest number of other asteroids.
# The idea is to load the asteroids in a list of coordinate pairs (x,y)
# Check all asteroids:
# - Find all the polar coordinates (angle, distance) between every other asteroid
# - Determine how many *distinct* angles there are
# - Find the maximum and return coordinates of that asteroid
# -*- coding: cp1252 -*-

import time
import numpy as np
import math

start = time.time()

asteroid_map = []
with open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_10.txt") as f:
    row = 0
    for line in f:
        #print line
        for col in range(len(line)):
            if line[col] == "#":
                if asteroid_map == []:
                    asteroid_map = [(col,row)]
                else:
                    asteroid_map.append((col,row))
        row += 1
    #print asteroid_map
    #print
    
max_asteroids = 0

for asteroid in asteroid_map:
    #print "Check asteroid:", asteroid 
    angle = []
    for other in asteroid_map:
        if other == asteroid:
            continue
        delta_x = asteroid[0] - other[0]
        delta_y = asteroid[1] - other[1]
        asteroid_angle    = math.pi + np.arctan2(delta_y, delta_x)
        asteroid_distance = np.sqrt (delta_x * delta_x + delta_y * delta_y)
        #print "With other:", other, "angle:", asteroid_angle, "distance:", asteroid_distance
        if (asteroid_angle in angle) == False:
            # First time this angle, add it
            angle.append(asteroid_angle)
            #print "First time", angle
        #else:
            #print "Already available"
        
    if max_asteroids == 0 or len(angle) > max_asteroids:
        max_asteroids = len(angle)
        max_asteroid = asteroid
        #print "New maximum:", max_asteroids, "for asteroid:", max_asteroid

print "Solution 1:", max_asteroid, max_asteroids

# Dict with asteroids per angel
angels = {}
asteroid = max_asteroid

angle = []
for other in asteroid_map:
    if other == asteroid:
        continue
    delta_x = asteroid[0] - other[0]
    delta_y = asteroid[1] - other[1]
    asteroid_angle    = math.pi + np.arctan2(delta_y, delta_x)
    asteroid_distance = np.sqrt (delta_x * delta_x + delta_y * delta_y)
    #print "With other:", other, "angle:", asteroid_angle, "distance:", asteroid_distance
    if (asteroid_angle in angle) == False:
        # First time this angle, add it
        angle.append(asteroid_angle)
        #print "First time", angle
    #else:
        #print "Already available"
    if (asteroid_angle in angels) == False:
        angels.update( {asteroid_angle : [(asteroid_distance, other)]})
    else:
        prev = list(angels.get(asteroid_angle))
        prev.append((asteroid_distance, other))
        angels.update ({asteroid_angle : prev})

for key in sorted(angels.keys()):
    print key, angels.get(key)

vaporized = 0
start_angle = 1.5 # Start at 90 degrees
while vaporized < 200:
    for key in sorted(angels.keys()):
        if (key / math.pi) >= start_angle:
            #print key, "-->", angels.get(key)
            asteroid_list = angels.get(key)
            min_distance = 0
            for asteroid in asteroid_list:
                if min_distance == 0 or asteroid[0] < min_distance:
                    min_distance = asteroid[0]
                    min_asteroid = asteroid[1]
            vaporized += 1
            print vaporized, min_asteroid
            # Remove this asteroid from the dict.key
            # Implementation wasn't needed because before a whole turn
            # 200 asteroids had already been vaporized
            if vaporized == 200:
                break
    for key in sorted(angels.keys()):
            #print key, "-->", angels.get(key)
            asteroid_list = angels.get(key)
            min_distance = 0
            for asteroid in asteroid_list:
                if min_distance == 0 or asteroid[0] < min_distance:
                    min_distance = asteroid[0]
                    min_asteroid = asteroid[1]
            vaporized += 1
            print vaporized, min_asteroid
            if vaporized == 200:
                break

print "Solution 2:", vaporized, min_asteroid, min_asteroid[0] * 100 + min_asteroid[1]

end = time.time()

print "Found solutions in:", end - start, "seconds"
