# How the input() Function Works

# Writing Clear Prompts
# message = input("Tell something, and I will repeat it back: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"Hello, {name}")

# prompt = "If you tell me your name, we can personalize your message."
# prompt += "\nWhat is your name? " # prompt = prompt + "\nWhat is your name? "
# name = input(prompt)

# print(f"Hello, {name}")

# Using int() to Accept Numerical Input
# age = input("Tell me your age: ")
# age = int(age)

# if age >= 18:
#     print("U r allowed")

# print(type(age))

# The Modulo Operator
number = input("Enter a number: ")
number = int(number)
if number % 2 == 0 :
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

print(number % 2)
