input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_1.txt")

total_fuel = 0
total_fuel_fuel = 0

for line in input_file:
    mass = int(line)
    fuel = mass / 3 - 2
    total_fuel += fuel
    total_fuel_fuel += fuel

    fuel_fuel = fuel
    while fuel_fuel > 6:
        add_fuel = fuel_fuel / 3 - 2
        total_fuel_fuel += add_fuel
        fuel_fuel = add_fuel

print total_fuel, total_fuel_fuel
