# Accessing Elements in a List
bycycles = ['trek', 'duronto', 'redline', 'connondale']
# print(bycycles)

# Index Positions Start at 0, Not 1
# print(bycycles[0].title())
# print(bycycles[3].title())

# Using Individual Values from a List
my_fav_bycycle = f'My favourite bycle is {bycycles[1].title()}.'
# print(my_fav_bycycle)

# Modifying Elements in a List
bycycles[3] = "chines"
# print(bycycles)

# Adding Elements to a List
motorcycles = ['honda', 'yamah', 'bajaj']
# print(motorcycles)
# Appending Elements to the End of a List
motorcycles.append("suzuki")
# print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(1, 'ducati')
# print(motorcycles)

# Removing Elements from a List
# Removing an Item Using the `del` Statement
del motorcycles[4]
# print(motorcycles)

# Removing an Item Using the pop() Method
# print(f'Before poped {motorcycles}')
poped_motorcycle = motorcycles.pop()
# print(f'After poped {motorcycles}')
# print(f'Poped motorcycle {poped_motorcycle}')

# Popping Items from any Position in a List
pop_index_1_motorcycle = motorcycles.pop(1)
# print(f"After poped at index 1 ({pop_index_1_motorcycle}) : {motorcycles}")

# Removing an Item by Value
# print(f"Befor removing 'yamah' : {motorcycles}")
motorcycles.remove('yamah')
# print(f"After removing 'yamah' : {motorcycles}")

# Organizing a List
cars = ['bmw', 'audi', 'ford', 'subaru']
## Sorting a List Permanently with the sort() Method
# print(f"Before sort, cars={cars}")
# cars.sort()
# print(f"After sort, cars={cars}")

# Sorting a List Temporarily with the sorted() Function
# print(f"Sorting List of cars using sorted method: {sorted(cars)}")
sorted_cars = sorted(cars)
# print(sorted_cars)
# print(f"After appling sorted method, cars={cars}")

# Printing a List in Reverse Order
cars.sort(reverse=True)
# print(f"Parmanently sort cars in reverse order: {cars}")

numbers = [12, 45, 4, 67, 4, 0, -23]
# print(numbers)
# parmanently
# numbers.sort(reverse=True)
print(numbers)

# temporarily
reverse_numbers = sorted(numbers, reverse=True)
# print(reverse_numbers)

# Finding the Length of a List
print(len(numbers))


# Avoiding Index Errors When Working with Lists
print(numbers[6])

# last element 
print(f"Last item : {numbers[-1]}")