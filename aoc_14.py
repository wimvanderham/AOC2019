# AOC 2019 - Day 14 - Space Stoichiometry - Get some FUEL

import time

start = time.time()

# Recipes for resulting elements is a dictionary
recipe = {}
with open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_14.txt") as f:
    # Read input of format:
    # 10 ORE => 10 A
    # 1 ORE => 1 B
    # 7 A, 1 B => 1 C
    # 7 A, 1 C => 1 D
    # 7 A, 1 D => 1 E
    # 7 A, 1 E => 1 FUEL
    # Store in recipe dictionary with key resulting element and
    # first attribute = quantity produced of resulting element
    # second and third attribute = element and quantity required
    # repeat for next elements
    for line in f:
        #print line
        element_list = []
        wordlist = line.rstrip().split(" ")
        #print "Wordlist:", wordlist
        result = wordlist[len(wordlist) - 1]
        #print result
        quantity = int(wordlist[len(wordlist) - 2])
        #print quantity
        element_list.append(quantity)
        for index in range(0,len(wordlist) - 3, 2):
            quantity = int(wordlist[index])
            element = wordlist[index + 1].rstrip(",")
            #print element, quantity
            element_list.append(element)
            element_list.append(quantity)
    
        if (result in recipe) == False: 
            # Add new result to dictionary
            recipe[result] = element_list
    #print "Starting situation:", recipe

stock = {}

def produce(element, require_quantity):
    if element in recipe:
        # There's a recipe for this element
        element_list = recipe.get(element)
    
        # Quantity produced
        quantity = int(element_list[0])
        #print "For:", quantity, "x", element, "require:",
        
        # Check stock
        if element in stock:
            stock_quantity = stock.get(element)
            require_quantity -= stock_quantity
            stock[element] -= stock_quantity
        else:
            stock[element] = 0

        recipe_quantity = int(require_quantity / quantity)
        if recipe_quantity * quantity < require_quantity:
            recipe_quantity += 1
            extra_quantity = (recipe_quantity * quantity) - require_quantity
            stock[element] += extra_quantity
        for index in range(1, len(element_list), 2):
            sub_element  = element_list[index]
            sub_quantity = element_list[index + 1]
            #print sub_quantity, "x", sub_element
            #print "Produce:", sub_element, recipe_quantity * sub_quantity
            produce(sub_element, recipe_quantity * sub_quantity)
    else:
        if element in stock:
            stock[element] = stock.get(element) + require_quantity
        else:
            stock[element] = require_quantity
        #print stock
    
produce("FUEL", 1)

end = time.time()

print "Found solution 1 in ", end - start, "seconds"

print "Solution 1:", stock["ORE"]

# Part 2: Calculate FUEL from a trillion units of ORE
max_ORE = 1000000000000

fuel = 2
step = 2
max_fuel = 0
step_1 = 0
while True:
    stock = {}
    produce("FUEL", fuel)
    if max_fuel == 0 or (fuel > max_fuel and stock["ORE"] <= max_ORE):
       max_fuel = fuel
    #print "Fuel:", fuel, "ORE:", stock["ORE"], "step:", step, "Direction:", direction, "max fuel:", max_fuel
    if stock["ORE"] > max_ORE:
        if step > 1:
            step = step / 2
        else:
            step_1 += 1
            if step_1 == 3:
                # After three step with length 1, we've reached our goal
                break
        fuel = fuel - step
    else:
        step = step * 2
        fuel = fuel + step
    

end = time.time()        

print "Found Solution 2 in", end - start, "seconds"
print "Solution 2:", max_fuel            

