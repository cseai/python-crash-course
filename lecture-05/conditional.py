cars = ['audi', 'Bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    # print(car)

if True:
    print('This is always true.')

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    # print(car)

ages = [4, 10, 18, 35, 55, 65]

for age in ages:
    if age != 18:
        print(f"You are not 18. Your age is {age}")
    
    # print(age)
for age in ages:
    if age < 18:
        print(f"You are a child {age}")
    
    if age >= 18:
        print(f"You are {age} years old")

for age in ages:
    if age >= 10 and age <= 55:
        print(f"Your age ({age}) is between [10, 55]")

for age in ages:
    if age <= 10 or age > 55:
        print(f"You should take rest [{age}]")

foods = ["apple", "pizza", "banana", "grillll", "pizza"]

if "pizza" in foods:
    print(f"I got it!")

if "laddu" not in foods:
    print("Laddu not found")