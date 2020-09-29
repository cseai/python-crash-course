# Return Values

# Returning a Simple Value
# def get_formatted_name(first_name, last_name):
#     """Return a full name"""
#     full_name = f"{first_name} {last_name}"

#     return full_name.title()

# my_friend_name = get_formatted_name("sahriar", "kabir")

# print(my_friend_name)

# Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

# my_name = get_formatted_name("belal", "hossain")
# my_name = get_formatted_name("md", "belal", "hossain")
# print(my_name)
# my_name = get_formatted_name("md", "hossain", "belal")
# print(my_name)

# my_name = get_formatted_name(first_name="md", middle_name="belal", last_name="hossain")
# print(my_name)

# Returning a Dictionary
def build_persone(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

# person_dic = build_persone("Sakib", "Hasan")
# print(person_dic)

# person_dic = build_persone("Sakib", "Hasan", 22)
# print(person_dic)

# Using a Function with a while Loop
while True:
    print("Please tell me your name:")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}")
