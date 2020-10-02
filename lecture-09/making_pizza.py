# Importing an Entire Module
# import pizza

# pizza.make_pizza(12, 'pepperoni')
# pizza.make_pizza(16, 'abc', 'sss', 'rrr')

# Importing Specific Functions
# from pizza import make_pizza, say_hi
# from pizza import make_pizza

# make_pizza(12, 'pepperoni')
# make_pizza(16, 'abc', 'sss', 'rrr')

# Using as to Give a Function an Alias
# from pizza import  make_pizza as mp

# mp(12, 'pepperoni')
# mp(16, 'abc', 'sss', 'rrr')

# Using as to Give a Module an Alias
# import pizza as p

# p.make_pizza(12, 'pepperoni')
# p.make_pizza(16, 'abc', 'sss', 'rrr')


# Importing All Functions in a Module
from pizza import *

# def say_hi():
#     print("Hey, I am eatting pizza!!")


make_pizza(12, 'pepperoni')
make_pizza(16, 'abc', 'sss', 'rrr')
say_hi()
say_hi()

# Styling Functions