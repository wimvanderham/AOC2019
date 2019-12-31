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
    name_opcode = {1: "add", 2: "mul", 3: "rcv", 4: "snd", 5: "beq", 6: "bne", 7: "slt", 8: "seq", 9: "arb", 99: "hlt"}
    
    #pos = 0
    while True:
        instruction = prog[pos]
        opcode = instruction % 100
        if opcode == 99:
            break

        instruction = instruction / 100
        parameter_mode = [0, 0, 0]
        parameter_mode[0] = instruction % 10
        instruction = instruction / 10
        parameter_mode[1] = instruction % 10
        instruction = instruction / 10
        parameter_mode[2] = instruction % 10

        # Make sure program memory is large enough
        if parameter_mode[0] == 0 and num_parameters.get(opcode) >= 1:
            while len(prog) <= prog[pos + 1]:
                prog.append(0)
        if parameter_mode[1] == 0 and num_parameters.get(opcode) >= 2:
            while len(prog) <= prog[pos + 2]:
                prog.append(0)
        if parameter_mode[2] == 0 and num_parameters.get(opcode) >= 3:
            while len(prog) <= prog[pos + 3]:
                prog.append(0)

        if parameter_mode[0] == 1 and num_parameters.get(opcode) >= 1 and opcode != 4:
            while len(prog) <= prog[pos + 1]:
                prog.append(0)
                
        if parameter_mode[0] == 2 and num_parameters.get(opcode) >= 1:
            while len(prog) <= relative_base + prog[pos + 1]:
                prog.append(0)
        if parameter_mode[1] == 2 and num_parameters.get(opcode) >= 2:
            while len(prog) <= relative_base + prog[pos + 2]:
                prog.append(0)
        if parameter_mode[2] == 2 and num_parameters.get(opcode) >= 3:
            while len(prog) <= relative_base + prog[pos + 3]:
                prog.append(0)
        #print
        #print "Pos:", pos, "instruction:", prog[pos], "opcode:", opcode, name_opcode[opcode], "num_parameters:", num_parameters.get(opcode),
        #for param in range(num_parameters.get(opcode)):
            #print "Param", param + 1, prog[pos + param + 1], parameter_mode[param]
            #if param == range(num_parameters.get(opcode)):
                #print
        #while True:
            #address = raw_input()
            #if address != "":
                #print "prog[" + address + "] = ", prog[int(address)]
            #else:
                #break
            
        
        #for index in range(num_parameters.get(opcode)):
            #print "Parameter_mode:", index, parameter_mode[index],
            #if parameter_mode[index] == 0:
            #    print "from pos:", prog[pos + index + 1], "value:", prog[prog[pos + index + 1]]
            #elif parameter_mode[index] == 1:
            #    print "take direct value from pos:", pos + index + 1, "=", prog[pos + index + 1]
            #elif parameter_mode[index] == 2:
            #    print "take from relative_base:", relative_base, "+ pos:", pos + index + 1, "=", prog[relative_base + index + prog[pos + 1]]
        #print "Press key to continue:",
        #raw_input()                                                                                            
                           

        #if opcode == 3:
            #print prog[pos], "opcode:", opcode, "pm[0]:", parameter_mode[0], "pm_2:", parameter_mode[1], "pm_3:", parameter_mode[2]
            #print "Length:", len(prog), "Parameter_1:", prog[pos + 1], "Num parameters opcode:", num_parameters.get(opcode), "Relative base:", relative_base
        

        if opcode == 1:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_out = prog[pos + 3]
            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
            result = operand_1 + operand_2
            if parameter_mode[2] == 2:
                prog[reg_out + relative_base] = result
            else:
                prog[reg_out] = result
            pos += 4
        if opcode == 2:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_out = prog[pos + 3]
            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
            result = operand_1 * operand_2
            if parameter_mode[2] == 2:
                prog[reg_out + relative_base] = result
            else:
                prog[reg_out] = result
            #print "Result:", result, "stored in:", reg_out, "=", prog[reg_out]
            pos += 4
        if opcode == 3:
            #print "Input at pos:", pos, "reg in =", prog[pos + 1]
            #print prog[pos], "opcode:", opcode, "pm[0]:", parameter_mode[0], "pm_2:", parameter_mode[1], "pm_3:", parameter_mode[2]
            #print "Which_input:", which_input, "Par 1:", input_parameter_1, "Par 2:", input_parameter_2
            reg_in = prog[pos + 1]
            if which_input == 1:
                if parameter_mode[0] == 0 or parameter_mode[0] == 1:
                    prog[reg_in] = input_parameter_1
                    #print "Stored:", input_parameter_1, "in:", reg_in
                elif parameter_mode[0] == 2:
                    prog[reg_in + relative_base] = input_parameter_1
                    #print "Stored:", input_parameter_1, "in:", relative_base + reg_in
                which_input = 2
            elif which_input == 2:
                if parameter_mode[0] == 0 or parameter_mode[0] == 1:
                    prog[reg_in] = input_parameter_2
                elif parameter_mode[0] == 2:
                    prog[reg_in + relative_base] = input_parameter_2
                which_input = 3
            else:
                print "Too much input requested"
                raw_input()
            pos += 2
        if opcode == 4:
            reg_out = prog[pos + 1]
            if parameter_mode[0] == 0:
                output_parameter = prog[reg_out]
            elif parameter_mode[0] == 1:
                output_parameter = reg_out
            elif parameter_mode[0] == 2:
                #print relative_base, reg_out
                output_parameter = prog[relative_base + reg_out]
            pos += 2
            #print "Output at pos:", pos - 2, output_parameter
            break
        if opcode == 5:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            
            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
                #print "[" + str(reg_in1) + "] = ", operand_1
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
                
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
            #print operand_1, "<>", 0, 
            #raw_input()
            if operand_1 <> 0:
                pos = operand_2
            else:
                pos += 3
            #print pos
        if opcode == 6:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
            if operand_1 == 0:
                pos = operand_2
            else:
                pos += 3
        if opcode == 7:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_in3 = prog[pos + 3]
            
            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
                
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
                
            if parameter_mode[2] == 0:
                operand_3 = reg_in3
            elif parameter_mode[2] == 1:
                operand_3 = reg_in3
            elif parameter_mode[2] == 2:
                operand_3 = reg_in3 + relative_base
                
            if operand_1 < operand_2:
                prog[operand_3] = 1
                #print "[" + str(operand_3) + "] = ", 1
            else:
                prog[operand_3] = 0
                #print "[" + str(operand_3) + "] = ", 0
            pos += 4
        if opcode == 8:
            reg_in1 = prog[pos + 1]
            reg_in2 = prog[pos + 2]
            reg_in3 = prog[pos + 3]

            #print "Parameters:", reg_in1,reg_in2, reg_in3 
            if parameter_mode[0] == 0:
                operand_1 = prog[reg_in1]
            elif parameter_mode[0] == 1:
                operand_1 = reg_in1
            elif parameter_mode[0] == 2:
                operand_1 = prog[reg_in1 + relative_base]
                
            if parameter_mode[1] == 0:
                operand_2 = prog[reg_in2]
            elif parameter_mode[1] == 1:
                operand_2 = reg_in2
            elif parameter_mode[1] == 2:
                operand_2 = prog[reg_in2 + relative_base]
                
            if parameter_mode[2] == 0:
                operand_3 = reg_in3
            elif parameter_mode[2] == 1:
                operand_3 = reg_in3
            elif parameter_mode[2] == 2:
                operand_3 = reg_in3 + relative_base
                
            #print "if", operand_1, "==", operand_2, "? [", operand_3, "] =", 1, "else", 0
            if operand_1 == operand_2:
                prog[operand_3] = 1
                #print operand_3, "=", 1
            else:
                prog[operand_3] = 0
                #print operand_3, "=", 0
            pos += 4
        if opcode == 9:
            reg_in1 = prog[pos + 1]
            #print "Relative before:", relative_base, "reg_in1:", reg_in1
            if parameter_mode[0] == 0:
                #print "Add 0:", reg_in1
                relative_base += prog[reg_in1]
            elif parameter_mode[0] == 1:
                #print "Add 1:", reg_in1
                relative_base += reg_in1
            elif parameter_mode[0] == 2:
                #print "Add 2:", prog[reg_in1 + relative_base]
                relative_base += prog[reg_in1 + relative_base]
            #print "New relative:", relative_base
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
print P, len(P)
output_list = []
while opcode <> 99:
    #print "opcode:", opcode, "pos:", pos
    output, opcode, pos, relative_base = calc_result(input_1, input_2, P, pos, relative_base)
    if opcode == 4:
        print "Output:", output
        #raw_input()
        output_list.append(output)
print
end = time.time()

print "Found Solutions 1 in:", (end - start)


# Part 2
start = time.time()
opcode = 0
pos = 0
relative_base = 0
input_1 = 2
input_2 = 0

P = list(program)
print P, len(P)
output_list = []
while opcode <> 99:
    #print "opcode:", opcode, "pos:", pos
    output, opcode, pos, relative_base = calc_result(input_1, input_2, P, pos, relative_base)
    if opcode == 4:
        print "Output 2:", output
        #raw_input()
        output_list.append(output)
print

print output_list
end = time.time()

print "Found Solutions 2 in:", (end - start)
