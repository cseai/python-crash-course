# Passing a List

def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

# usernames = ['belal', 'kabir', 'rafiq']
# greet_users(usernames)

# Modifying a List in a Function
# unprinted_designs = ['phone case', 'fan', 'small box']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# print("The following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'fan', 'small box']
completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)

# Preventing a Function from Modifying a List
unprinted_designs = ['phone case', 'fan', 'small box']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)