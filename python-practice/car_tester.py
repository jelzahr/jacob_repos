from car import Car

car_list = []

with open('cars.txt') as file:
    for line in file:
        stripped = line.strip()
        tokens = stripped.split()
        car_list.append(Car(tokens[0],tokens[1],int(tokens[2]),int(tokens[3])))

print(car_list[0])
print(car_list[1])

print('Gas in car 1 to start:', car_list[0].get_gas_tank())
print('Gas in car 2 to start:', car_list[1].get_gas_tank())

print('Miles on car 1 to start:', car_list[0].get_odometer())
print('Miles on car 2 to start:', car_list[1].get_odometer())

car_list[0].drive()
car_list[1].drive()

print('Gas in car 1 to finish:', car_list[0].get_gas_tank())
print('Gas in car 2 to finish:', car_list[1].get_gas_tank())

print('Miles on car 1 to finish:', car_list[0].get_odometer())
print('Miles on car 2 to finish:', car_list[1].get_odometer())