# Defining a Function
# def greet_user():
#     """Display a simple message"""
#     print("Hello")

# greet_user()


# Passing Information to a Function
def greet_user(username):
    """Display a simple message"""
    print(f"Hello, {username.title()} ")

# Arguments and Parameters
# greet_user("belal")

# Passing Arguments

# Positional Arguments
# def describe_pet(animal_type, pet_name):
#     """Describing about a pet"""
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# Positional Arguments
# describe_pet("cat", "kitty")

# Order Matters in Positional Arguments
# describe_pet("kitty", "cat")

# Keyword Arguments
# describe_pet(animal_type="cat", pet_name="kitty")
# describe_pet(pet_name="kitty", animal_type="cat")

# Default Values
def describe_pet(pet_name, animal_type="cat"):
    """Describing about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet("kitty")
# describe_pet("doggy", "dog")

# Equivalent Function Calls
# describe_pet(animal_type="cat", pet_name="kitty")
# describe_pet(pet_name="kitty", animal_type="cat")
# describe_pet(pet_name="mini kitty")

# describe_pet("kitty")
# describe_pet("doggy", "dog")

# Avoiding Argument Errors
# describe_pet()