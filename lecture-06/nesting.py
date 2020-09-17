# Nesting

# A List of Dictionaries

alien_0 = {'color': 'green', 'points': 4}
alien_1 = {'color': 'yellow', 'points': 343}
alien_2 = {'color': 'green', 'points': 34}
alien_3 = {'color': 'red', 'points': 44}

aliens = [alien_0, alien_1, alien_2, alien_3]

# print(aliens)

# A List in a Dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# print(pizza['toppings'])

# A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

# print(users)
print(users['aeinstein']['first'])