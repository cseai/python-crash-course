# Working with Part of a List
players = ["sakib", "moshfiq", "rubel", "nasir", "nafiz"]

# Slicing a List
# print(players[0:2])

# print(players[ :2])

# print(players[1:3])

# print(players[-4:])
# print(players[-4:-1])

# print(players[-4:-2])

# Looping Through a Slice
# numbers = [10, 234, 4, 56, 78, 34]
# for x in numbers[:4]:
#     print(x)

# Copying a List
my_foods = ["pizza", "grill", "coffee"]
# print(f"my_foods {my_foods}")

my_friend_foods = my_foods
# print(f"my_friend_foods {my_friend_foods}")

my_foods.append("lacchi")

# print(f"my_foods {my_foods}")
# print(f"my_friend_foods {my_friend_foods}")

# copy will work here
foods = ["pizza", "grill", "coffee"]
copied_foods = foods[:]
foods.append("lacchi")
# print(f"foods {foods}")
# print(f"foods copied {copied_foods}")

# Tuples
# Defining a Tuple
_a_touple = (0,)
print(type(_a_touple))
fixed_rectangle = (200, 100)
print(fixed_rectangle)

# fixed_rectangle[0] = 3000
# print(fixed_rectangle)

# Looping Through All Values in a Tuple
t_nums = (1, 3, 5, 7)
for t in t_nums:
    print(t)

# Writing over a Tuple
fixed_rectangle = (400, 200)
print(fixed_rectangle)