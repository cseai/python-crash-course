# Passing an Arbitrary Number of Arguments
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     # print(toppings)
#     print("List of toppings (requested):")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('abc', 'sss', 'rrr')

# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    # print(toppings)
    print(f"List of toppings (requested) of pizza size- {size} inc :")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza(12, 'pepperoni')
# make_pizza(16, 'abc', 'sss', 'rrr')

# Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('belal', 'hossain',
                    location="Naogaon",
                    field="Engg")
print(user_profile)

