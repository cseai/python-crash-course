# Introducing while Loops

# The while Loop in Action
# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1


# Letting the User Choose When to Quit 
# msg = ''
# while msg != 'quit':
#     msg = input("Say something. type 'quit' to exit: ")
#     print(msg)

# Using a Flag
# active = True
# while active:
#     msg = input("Say something. type 'quit' or 'stop' or 'exit' to exit: ")

#     if msg == 'quit':
#         active = False
#     elif msg == 'stop':
#         active = False
#     elif msg == 'exit':
#         active = False
#     else:
#         print(msg)

# Using break to Exit a Loop
# while True:
#     msg = input("Say something. type 'quit' or 'stop' or 'exit' to exit: ")

#     if msg == 'quit':
#         break
#     elif msg == 'stop':
#         break
#     elif msg == 'exit':
#         break
#     else:
#         print(msg)


# Using continue in a Loop
# current_num = 0
# while current_num <= 10:
#     current_num += 1
#     if current_num % 2 == 0:
#         continue

#     print(f"{current_num} is odd")

# Avoiding Infinite Loops
# ctrl+ C
# x = 1
# while x <= 5:
#     print(x)

# Using a while Loop with Lists and Dictionaries

# Moving Items from One List to Another
# unconfirmed_users = ["belal", "kabir", "roki"]
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifyng user: {current_user}")

#     confirmed_users.append(current_user)

# print("Showing confirmed user:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user)

# print(unconfirmed_users)

# Removing All Instances of Specific Values from a List
# pets = ['cat', 'dog', 'got', 'rabbit', 'cat', 'dog', 'cat']

# print(pets)
# # pets.remove("cat")

# while 'cat' in pets:
#     pets.remove("cat")
#     # print("Removing cat...")
#     # print(pets)
# print(pets)


# Filling a Dictionary with User Input

responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("What is your favorite color? ")
    
    responses[name] = response

    repeat = input("Do you want another response? ('yes' or 'no'): ")

    if repeat == 'no':
        polling_active = False

print("Showing polling result:")

for name, response in responses.items():
    print(f"{name.title()}'s favorite color is {response}")