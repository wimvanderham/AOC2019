import time

program = []

def calc_result(input_parameter_1, input_parameter_2, prog):
    
    #print "CALC_RESULT:", input_parameter_1, input_parameter_2
    #print prog
    output_parameter = 0

    which_input = 1
    
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
            if which_input == 1:
                prog[reg_in] = input_parameter_1
                which_input = 2
            elif which_input == 2:
                prog[reg_in] = input_parameter_2
            else:
                print "Too much input requested"
                raw_input()
            pos += 2
        if opcode == 4:
            reg_out = prog[pos + 1]
            output_parameter = prog[reg_out]
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

input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_7.txt")
program = [int(x) for x in input_file.read().split(",")]

highest_signal = 0

for input_A in range(5):
    input_list = [input_A]
    print "A:", input_A, 0
    result_A = calc_result(input_A, 0, list(program))
    print "Result A:", result_A
    for input_B in range(5):
        if input_B in input_list:
            continue
        input_list.append(input_B)
        print "B:", input_B, result_A, input_list
        result_B = calc_result(input_B, result_A, list(program))
        print "Result B:", result_B
        for input_C in range(5):
            if input_C in input_list:
                continue
            input_list.append(input_C)
            print "C:", input_C, result_B, input_list
            result_C = calc_result(input_C, result_B, list(program))
            print "Result C:", result_C
            for input_D in range(5):
                if input_D in input_list:
                    continue
                input_list.append(input_D)
                print "D:", input_D, result_C, input_list
                result_D = calc_result(input_D, result_C, list(program))
                print "Result D:", result_D
                for input_E in range(5):
                    if input_E in input_list:
                        continue
                    input_list.append(input_E)
                    print "E:", input_E, result_D, input_list
                    result_E = calc_result(input_E, result_D, list(program))
                    print "Result E:", result_E
                    if highest_signal == 0 or result_E > highest_signal:
                        highest_signal = result_E
                        print "New high:", highest_signal, input_list
                        highest_combination = list(input_list)
                        raw_input()
                    # Remove E from the list
                    input_list.pop()
                # Remove D from the list
                input_list.pop()
            # Remove C from the list
            input_list.pop()
        # Remove B from the list
        input_list.pop()
    # Remove A from the list
    input_list.pop()
    
print "Solution 1:", highest_combination, "productes:", highest_signal

end = time.time()


print "Found Solutions in:", (end - start)





    
