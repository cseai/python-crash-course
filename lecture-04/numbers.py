# Making Numerical Lists
# Using the range() Function
for value in range(1,5):
    print(value)

# Using range() to Make a List of Numbers

N_numbers = list(range(1, 11))
print(N_numbers)

Even_numbers = list(range(2, 11, 2))
print(Even_numbers)

num_data = [12, 34, 5, 0, 39000]
print(f"Min number : {min(num_data)}")

print(f"Max number : {max(num_data)}")

print(f"Sum number : {sum(num_data)}")

# square of natural number
squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)

print(squares)

# List Comprehensions
N_squares = [ value ** 2 for value in range(1, 11) ]
print(f"List comprehension n_squares value: {N_squares}")