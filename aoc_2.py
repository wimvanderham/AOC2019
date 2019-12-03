input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_2.txt")

program = []
program = [int(x) for x in input_file.read().split(",")]

#print program

# Change start condition
program[1] = 12
program[2] = 2

pos = 0
while program[pos] <> 99:
    opcode = program[pos]
    if opcode == 1:
        reg_in1 = program[pos + 1]
        reg_in2 = program[pos + 2]
        reg_out = program[pos + 3]
        result = program[reg_in1] + program[reg_in2]
        program[reg_out] = result
        pos += 4
    if opcode == 2:
        reg_in1 = program[pos + 1]
        reg_in2 = program[pos + 2]
        reg_out = program[pos + 3]
        result = program[reg_in1] * program[reg_in2]
        program[reg_out] = result
        pos += 4

print program[0]
    
