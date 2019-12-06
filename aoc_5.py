import time

program = []

def calc_result(input_parameter, prog):
    
    print "CALC_RESULT:", input_parameter
    print prog
    output_parameter = 0
    
    pos = 0
    while True:
        instruction = prog[pos]
        opcode = instruction % 100
        if opcode == 99:
            break
        instruction = instruction / 100
        parameter_mode_1 = instruction % 10
        instruction = instruction / 10
        parameter_mode_2 = instruction % 10
        instruction = instruction / 10
        parameter_mode_3 = instruction % 10

        #print prog[pos], "opcode:", opcode, "pm_1:", parameter_mode_1, "pm_2:", parameter_mode_2, "pm_3:", parameter_mode_3
        
        if opcode == 1:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_out = prog[pos + 3]
            if parameter_mode_1 == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode_1 == 1:
                operand_1 = reg_in1
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            result = operand_1 + operand_2
            prog[reg_out] = result
            pos += 4
        if opcode == 2:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_out = prog[pos + 3]
            if parameter_mode_1 == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode_1 == 1:
                operand_1 = reg_in1
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            result = operand_1 * operand_2
            prog[reg_out] = result
            pos += 4
        if opcode == 3:
            reg_in = prog[pos + 1]
            prog[reg_in] = input_parameter
            pos += 2
        if opcode == 4:
            reg_out = prog[pos + 1]
            output_parameter = prog[reg_out]
            pos += 2
        if opcode == 5:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            if parameter_mode_1 == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode_1 == 1:
                operand_1 = reg_in1
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            if operand_1 <> 0:
                pos = operand_2
            else:
                pos += 3
        if opcode == 6:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            if parameter_mode_1 == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode_1 == 1:
                operand_1 = reg_in1
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            if operand_1 == 0:
                pos = operand_2
            else:
                pos += 3
        if opcode == 7:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_in3 = prog[pos + 3]
            if parameter_mode_1 == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode_1 == 1:
                operand_1 = reg_in1
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            if parameter_mode_3 == 0:
                operand_3 = reg_in3
            elif parameter_mode_3 == 1:
                operand_3 = reg_in3
            if operand_1 < operand_2:
                prog[operand_3] = 1
            else:
                prog[operand_3] = 0
            pos += 4
        if opcode == 8:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_in3 = prog[pos + 3]
            #print "Parameters:", reg_in1, reg_in2, reg_in3
            if parameter_mode_1 == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode_1 == 1:
                operand_1 = reg_in1
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            if parameter_mode_3 == 0:
                operand_3 = reg_in3
            elif parameter_mode_3 == 1:
                operand_3 = reg_in3
            #print "if", operand_1, "==", operand_2, "? [", operand_3, "] =", 1, "else", 0
            if operand_1 == operand_2:
                prog[operand_3] = 1
            else:
                prog[operand_3] = 0
            pos += 4

        #print prog
        
    return output_parameter

start = time.time()

input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_5.txt")
program = [int(x) for x in input_file.read().split(",")]


result_1 = calc_result(1, list(program))
print "Solution 1:", result_1

result_2 = calc_result(5, list(program))
print "Solution 2:", result_2

end = time.time()


print "Found Solutions in:", (end - start)





    
