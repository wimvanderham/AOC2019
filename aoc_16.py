# AOC 2019 - Day 16 - Flawed Frequency Transmission - Calculate FFF

import time

start = time.time()

with open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_16.txt") as f:
    # Read input
    for line in f:
        input_string = line.strip()
    print "Starting input:", list(input_string)


def get_output(input_string, pattern):
    output_string = ""
    for new_index in range(len(input_string)):
        # Create pattern
        #print "Create pattern for:", new_index
        input_pattern = []
        input_pattern_pos = 0
        get_pattern_pos   = 0
        get_pattern_count = 0
        while input_pattern_pos <= len(input_string):
            #print "while:", input_pattern_pos, "<", len(input_string)
            input_pattern.append(pattern[get_pattern_pos])
            input_pattern_pos += 1
            get_pattern_count += 1
            if get_pattern_count > new_index:
                get_pattern_count = 0
                get_pattern_pos += 1
            if get_pattern_pos == len(pattern):
                get_pattern_pos = 0
            #print input_pattern_pos, new_index, input_pattern, get_pattern_pos, input_pattern_pos
        # Calculate output_string
        new_output = 0
        for index in range(len(input_string)):
            output = int(input_string[index]) * input_pattern[index + 1]
            new_output += output
        new_output = abs(new_output) % 10
        output_string = output_string + str(new_output)
        
    return output_string

for phase in range(100):
    output_string = get_output(input_string, [0, 1, 0, -1])
    #print phase, input_string, output_string
    input_string = output_string

end = time.time()

print "Found solution 1 in ", end - start, "seconds"

print "Solution 1:", output_string[0:8]

