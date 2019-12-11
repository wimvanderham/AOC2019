import time

program = []

def calc_result(input_parameter_1, input_parameter_2, prog, pos, relative_base):
    
    #print "CALC_RESULT:", input_parameter_1, input_parameter_2
    #print prog
    #print pos, len(prog)
    #raw_input()
    
    output_parameter = 0

    which_input = 1

    # Define a dict with the number of parameters for each opcode
    num_parameters = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1}
    
    #pos = 0
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

        if opcode == 3:
            print prog[pos], "opcode:", opcode, "pm_1:", parameter_mode_1, "pm_2:", parameter_mode_2, "pm_3:", parameter_mode_3
            print "Length:", len(prog), "Parameter_1:", prog[pos + 1], "Num parameters opcode:", num_parameters.get(opcode), "Relative base:", relative_base
        
        if parameter_mode_1 == 0 and num_parameters.get(opcode) >= 1:
            while len(prog) <= prog[pos + 1]:
                prog.append(0)
        if parameter_mode_2 == 0 and num_parameters.get(opcode) >= 2:
            while len(prog) <= prog[pos + 2]:
                prog.append(0)
        if parameter_mode_3 == 0 and num_parameters.get(opcode) >= 3:
            while len(prog) <= prog[pos + 3]:
                prog.append(0)

        if parameter_mode_1 == 2 and num_parameters.get(opcode) >= 1:
            while len(prog) <= relative_base + prog[pos + 1]:
                prog.append(0)

        if opcode == 1:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_out = prog[pos + 3]
            if parameter_mode_1 == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode_1 == 1:
                operand_1 = reg_in1
            elif parameter_mode_1 == 2:
                operand_1 = prog[relative_base + reg_in1]
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            elif parameter_mode_2 == 2:
                operand_2 = prog[relative_base + reg_in2]
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
            elif parameter_mode_1 == 2:
                operand_1 = prog[relative_base + reg_in1]
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            elif parameter_mode_2 == 2:
                operand_2 = prog[relative_base + reg_in2]
            result = operand_1 * operand_2
            prog[reg_out] = result
            #print "Result:", result, "stored in:", reg_out, "=", prog[reg_out]
            pos += 4
        if opcode == 3:
            print "Input at pos:", pos, "reg in =", prog[pos + 1]
            print prog[pos], "opcode:", opcode, "pm_1:", parameter_mode_1, "pm_2:", parameter_mode_2, "pm_3:", parameter_mode_3
            print "Which_input:", which_input, "Par 1:", input_parameter_1, "Par 2:", input_parameter_2
            reg_in = prog[pos + 1]
            if which_input == 1:
                if parameter_mode_1 == 0 or parameter_mode_1 == 1:
                    prog[reg_in] = input_parameter_1
                elif parameter_mode_1 == 2:
                    prog[relative_base + reg_in] = input_parameter_1
                which_input = 2
            elif which_input == 2:
                if parameter_mode_1 == 0 or parameter_mode_1 == 1:
                    prog[reg_in] = input_parameter_2
                elif parameter_mode_1 == 2:
                    prog[relative_base + reg_in] = input_parameter_2
                which_input = 3
            else:
                print "Too much input requested"
                raw_input()
            print "Stored:", prog[reg_in], "in:", reg_in
            pos += 2
        if opcode == 4:
            reg_out = prog[pos + 1]
            if parameter_mode_1 == 0:
                output_parameter = prog[reg_out]
            elif parameter_mode_1 == 1:
                output_parameter = reg_out
            elif parameter_mode_1 == 2:
                output_parameter = prog[relative_base + reg_out]
            pos += 2
            print "Output at pos:", pos - 2, output_parameter
            break
        if opcode == 5:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            if parameter_mode_1 == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode_1 == 1:
                operand_1 = reg_in1
            elif parameter_mode_1 == 2:
                operand_1 = prog[relative_base + reg_in1]
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            elif parameter_mode_2 == 2:
                operand_2 = prog[relative_base + reg_in2]
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
            elif parameter_mode_1 == 2:
                operand_1 = prog[relative_base + reg_in1]
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            elif parameter_mode_2 == 2:
                operand_2 = prog[relative_base + reg_in2]
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
            elif parameter_mode_1 == 2:
                operand_1 = prog[relative_base + reg_in1]
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            elif parameter_mode_2 == 2:
                operand_3 = prog[relative_base + reg_in2]
            if parameter_mode_3 == 0:
                operand_3 = reg_in3
            elif parameter_mode_3 == 1:
                operand_3 = reg_in3
            elif parameter_mode_3 == 2:
                operand_3 = prog[relative_base + reg_in3]
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
            elif parameter_mode_1 == 2:
                operand_1 = prog[relative_base + reg_in1]
            if parameter_mode_2 == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode_2 == 1:
                operand_2 = reg_in2
            elif parameter_mode_2 == 2:
                operand_2 = prog[relative_base + reg_in2]
            if parameter_mode_3 == 0:
                operand_3 = reg_in3
            elif parameter_mode_3 == 1:
                operand_3 = reg_in3
            elif parameter_mode_3 == 2:
                operand_3 = prog[relative_base + reg_in3]
            #print "if", operand_1, "==", operand_2, "? [", operand_3, "] =", 1, "else", 0
            if operand_1 == operand_2:
                prog[operand_3] = 1
            else:
                prog[operand_3] = 0
            pos += 4
        if opcode == 9:
            reg_in1 = prog[pos + 1]
            relative_base += reg_in1
            pos += 2

        #print prog
        
    return output_parameter, opcode, pos, relative_base

# ---- MAIN ----
start = time.time()

input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_9.txt")
program = [int(x) for x in input_file.read().split(",")]

opcode = 0
pos = 0
relative_base = 0
input_1 = 1
input_2 = 0

P = list(program)
print P
while opcode <> 99:
    #print "opcode:", opcode, "pos:", pos
    output, opcode, pos, relative_base = calc_result(input_1, input_2, P, pos, relative_base)
    if opcode == 4:
        print "Output:", output
print

end = time.time()

print "Found Solutions in:", (end - start)
