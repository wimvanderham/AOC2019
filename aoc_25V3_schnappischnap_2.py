# Day 25 - Cryostasis - Text adventure
# Intcode part created by Benjamin Watson (schnappischnap) and stored on github:
# https://github.com/schnappischnap/advent_of_code_2019/blob/master/day_19_tractor_beam.py
# I added the command recording and made changes to the input 03 and output 04 opcode's
# The program can run in two modes:
# Interactively (just leave the input_list = []
# Automatic (once you found the path to the Security Checkpoint and the usable items
# Have fun! I did ;-)

from collections import defaultdict

class Intcode:
    def __init__(self, data, values=None):
        self.prog = defaultdict(int)
        for i, j in enumerate(map(int, data.split(","))):
            self.prog[i] = j
        if values is None:
            self.values = []
        else:
            self.values = values
        self.pos = 0
        self.rel_base = 0
        self.output = None
        self.cmds = []

    def set(self, i, v, mode):
        if mode == "0":
            self.prog[self.prog[self.pos+i]] = v
        else:
            self.prog[self.prog[self.pos+i]+self.rel_base] = v

    def get(self, i, mode):
        if mode == "0":
            return self.prog[self.prog[self.pos+i]]
        elif mode == "1":
            return self.prog[self.pos+i]
        elif mode == "2":
            return self.prog[self.prog[self.pos+i]+self.rel_base]

    # Function to record commands
    def addcmd(self, cmd):
        self.cmds.append(cmd)
        #print (self.cmds)

    # Function to return recorded commands
    def getcmds(self):
        return self.cmds
    
    def run(self):
        output_string = ""
        while True:
            instruction = str(self.prog[self.pos]).zfill(5)
            opcode = instruction[3:]
            modes = list(reversed(instruction[:3]))

            #print (instruction, opcode, modes, self.pos)
            
            a, b = None, None
            try:
                a = self.get(1, modes[0])
                b = self.get(2, modes[1])
            except IndexError:
                pass

            if opcode == "01":
                self.set(3, a + b, modes[2])
                self.pos += 4
            elif opcode == "02":
                self.set(3, a * b, modes[2])
                self.pos += 4
            elif opcode == "03":
                if len(self.values) == 0:
                    #print (output_string)
                    #output_string = ""
                    input_string = input()
                    if input_string == "quit" or input_string == "bye" or input_string == "q" or input_string == "exit":
                        # One of these inputs will output the recorded commands and stop processing
                        print (self.cmds)
                        return
                    self.addcmd(input_string)
                    self.values = getASCIIList(input_string)
                    yield None
                self.set(1, self.values.pop(0), modes[0])
                self.pos += 2
            elif opcode == "04":
                yield self.get(1, modes[0])
                self.output = self.get(1, modes[0])
                self.pos += 2
                if self.output == 10:
                    print (output_string)
                    output_string = ""
                else:
                    output_string += chr(self.output)
            elif opcode == "05":
                self.pos = b if a != 0 else self.pos+3
            elif opcode == "06":
                self.pos = b if a == 0 else self.pos+3
            elif opcode == "07":
                self.set(3, 1 if a < b else 0, modes[2])
                self.pos += 4
            elif opcode == "08":
                self.set(3, 1 if a == b else 0, modes[2])
                self.pos += 4
            elif opcode == "09":
                self.rel_base += a
                self.pos += 2
            else:
                assert opcode == "99"
                #return self.output
                return output_string

def getASCIIList(string):
    ASCII_list = []
    for char in string:
        ASCII_list.append(ord(char))
    ASCII_list.append(10)
    return ASCII_list

def getASCIIString(ASCII_list):
    ASCII_string = ""
    for char in ASCII_list:
        ASCII_string += ord(int(char))
    return ASCII_string

def getCombItems(list_items, combination):
    # Return all possible unique combinations from a list of input items
    sub_list = []
    # Transform number to binary to get switches (0 or 1)
    # while adding up one more then the 2^number to get prefix 0's
    # and only using the final part (the first binary number will be 1 but only
    # served to fill up the initial 0's of the smaller numbers
    switches = format(combination + (2**len(list_items) + 1), "b")[1:]
    for position in range(len(list_items)):
        if switches[position] == "1":
            # Take this item
            sub_list.append(list_items[position])
    #print (combination, switches, sub_list)
    return sub_list
    
if __name__ == '__main__':
    input_list = []
    input_string = ""
    with open('C:\\Users\\Wim\\Documents\\AOC\\2019\\input_25.txt', 'r') as f:
        inp = f.read()

    # The path to the security check point passing every room with an item to take
    # Comment it out and you will enter in interactive mode
    input_list = ['west', 'take ornament', 'west', 'take astrolabe', 'north', 'take fuel cell', 'south', 'south', 'take hologram', 'north', 'east', 'south', 'east', 'take weather machine', 'west', 'north', 'east', 'east', 'take mug', 'north', 'take monolith', 'south', 'south', 'west', 'north', 'west', 'take bowl of rice', 'north', 'west', 'inv']
    # The item list you've gathered
    # This was my list, check carefully for your items
    item_list = ['bowl of rice', 'monolith', 'mug', 'weather machine', 'fuel cell', 'astrolabe', 'ornament', 'hologram']

    if input_list:
        # We have already discovered the path and the items
        print ("\nT E X T   A D V E N T U R E   -   A U T O M A T E D")
        print ("\nGo directly to the Security Checkpoint with all available items and then every combination to get through.\nSit back and relax, we'll get Santa out in a minute :-)\n")
        input("Press Return to start the automated navigation and Security passing. ")
        # At this point, first drop all items and try out every combination of the available items
        for item in item_list:
            input_list.append('drop ' + item)
        
        #input_list.append('inv')

        #print (item_list)
        for combination in range(2**len(item_list)):
            take_list = getCombItems(item_list, combination)
            for item in take_list:
                input_list.append('take ' + item)
            #input_list.append('inv')
            # Try to get through security check
            input_list.append('north')
            for item in take_list:
                input_list.append('drop ' + item)
    else:
        print ("\nT E X T   A D V E N T U R E   -   I N T E R A C T I V E")
        print ("\nStart the interactive text adventure.\nCommands will be recorded.\nIf you give 'quit' command they will be printed and execution is stopped.\n\nGood luck finding all the rooms, the usable items and the Security Check!\nBut be aware of some 'dangerous' items...")
    # Create input string transforming commands in ASCII integers per character
    input_string = []
    for command in input_list:
        input_string.extend(getASCIIList(command))
    
    output_string = ""
    while True:
        *_, output = Intcode(inp, input_string).run()

        #print (_, output)
        
        if output == 10:
            print (output_string)
            output_string = ""
            break
        else:
            output_string += chr(output)
        
