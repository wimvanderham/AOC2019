import time

program = []

def calc_result(noun, verb, prog):
    
    # Change start condition
    prog[1] = noun
    prog[2] = verb

    #print "CALC_RESULT:", prog
    
    pos = 0
    while prog[pos] <> 99:
        opcode = prog[pos]
        if opcode == 1:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_out = prog[pos + 3]
            # Add
            result = prog[reg_in1] + prog[reg_in2]
            prog[reg_out] = result
            pos += 4
        if opcode == 2:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_out = prog[pos + 3]
            # Multiply
            result = prog[reg_in1] * prog[reg_in2]
            prog[reg_out] = result
            pos += 4
    return prog[0]

start = time.time()

input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_2.txt")
program = [int(x) for x in input_file.read().split(",")]
result = 0
           
# Now find combination to find 19690720
find = 19690720
for noun in range(100):
    result_0 = calc_result(noun, 0, list(program))
    result_99 = calc_result(noun, 99, list(program))
    if result_0 < find and result_99 > find:
        # Right noun
        verb = find - result_0
        result = calc_result(noun, verb, list(program))
        if result == find:
            break
    if result == find:
        break
    
end = time.time()

print (end - start), "-->", noun * 100 + verb, result




    
