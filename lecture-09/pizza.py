# Storing Your Functions in Modules

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    # print(toppings)
    print(f"List of toppings (requested) of pizza size- {size} inc :")
    for topping in toppings:
        print(f"- {topping}")

def say_hi():
    print("Hi, I can make a pizza!!")