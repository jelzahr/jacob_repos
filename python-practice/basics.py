# string length
title = 'Rephactor Python'
print(len(title))

# string index positions
print('Last character:', title[-1])
print('Fifth character from the end:', title[-5])
print('Eighth character from the end:', title[-8])

# repetition operator
hashtags = 15 * '#'
print(hashtags)

# comparing strings
magician = 'Harry Houdini'
if magician == 'Harry Houdini':
    print("World's greatest magician!")
elif magician != 'Harry Houdini':
    print("Not Harry :(")

# dot operator
name = 'John'
name_in_uppercase = name.upper()
print(name_in_uppercase)

# membership operator
if 'love' in 'lovesick':
    print('Love can be found in unexpected places.')
if 'crying' not in 'baseball':
    print("There's no crying in baseball!")

today = 'Wednesday'
weekend = ['Saturday', 'Sunday']
if today in weekend:
    print("Hurray, it's the weekend!")
else:
    print("Everybody's working for the weekend!")

# for statement
sales = [32.75, 12.50, 24.18, 9.95, 27.32, 21.88]
total = 0
for amount in sales:
    total += amount
print('Total:', total)

for num in range(50, 60):       # range function
    print(num, end=' ')
for num in range(10, 0, -1):    # step value
    print(num, end=' ')

# while statement
num = float(input('Enter a number greater than 100: '))
while num <= 100:
    num = float(input('Invalid. Please reenter: '))
print('Moving on...')

# lists
lst = [10,20,30,40,50]
print('This is a list: ',lst)

# add elements
lst.append(5)
lst.append(6)
lst.append(7)
print('\nAppended three elements: ',lst)

# remove elements
lst.remove(40)
print('\nRemoving the number 40: ',lst)
lst.pop(2)
print('\nRemoving the index 2: ',lst)

# functions
lst.reverse()
print('\nReverse list: ',lst)
lst.sort()
print('\nSort list : ',lst)

# changing values
lst[0] = 500
print('\nChange value at index 0 to 500: ',lst)

# slicing
lst = lst[1:]
print('\nSlice off the first value: ',lst)

# index
index10 = lst.index(10)
print('\nIndex of the number 10 in the list: ',index10)

# count
lst.append(20)
lst.append(20)
lst.append(20)
print('\nAdd 20 three times to the list: ',lst)
count20 = lst.count(20)
print('and count how many times it appears in the list: ',count20)

# copying
print('\nINCORRECT copying of a list:')
copy_lst = lst # memory address is copied
print(copy_lst)
copy_lst[0] = 99
print(copy_lst)
print(lst)
### use copy method ###
print('CORRECT copying of a list using copy method:')
new_copy = lst.copy()
print(new_copy)
new_copy[0] = 5000
print(new_copy)
print(lst)

new_copy = lst[:]

# populate an empty list
empty_lst = []
for val in lst:
    empty_lst.append(val)
print('\nPopulated an empty list with a for loop: ',empty_lst)

# comprehension
squares = []
for i in range(1,10):
    squares.append(i**2)
print('\nMade without list comprehension: ',squares)

cubes = [x**3 for x in range(1,10)]
print('\nMade with list comprehension: ',cubes)

init_lst = [99,7,10,20,40,75,100,0]
plus5 = [x+5 for x in init_lst]
print(f'\n {init_lst} Using comprehension to add 5 to each element: ',plus5)

values = [34,2,95,18,36,21,64,50,17]
small_vals = [x for x in values if x<20]
print(f'\n {values} Optional if statement : ',small_vals)

# dictionaries
print('\nDictionaries: ')
fav_foods = {'Kathleen' : 'pizza', 'Hannah' : 'pasta', 
             'Kush' : 'fries', 'Yamill' : 'fries'}
    # keys must be unique, values can be repeated
print(fav_foods)
print("Hannah's favorite food: ", fav_foods['Hannah'])
    # two ways to iterate through list
print("\nPrint dictionary with a printf: ")
for key in fav_foods:
    print(f"\t{key}'s favorite food is {fav_foods[key]}")

print("\nPrint dictionary with items method: ")
for person, food in fav_foods.items():
    print(f"\t{person}'s favorite food is {food}")

if 'Bob' in fav_foods:
    print(fav_foods['Bob'])
else:
    fav_foods['Bob'] = 'wings'
print(fav_foods)

'''
OR USE:
if 'Bob' not in fav_foods:
    fav_foods['Bob'] = 'wings'
print(fav_foods)
'''

# sets
lst1 = [99,22,3,4,5,5,6,7,7,8]
set1 = set(lst1)
print(set1)