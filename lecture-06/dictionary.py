# A Simple Dictionary
# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# Working with Dictionaries
# alien_0 = {'color': 'green', 'points': 4}
# Accessing Values in a Dictionary

# new_points = alien_0['points']
# print(f"New point is {new_points} points")

# Adding New Key-Value Pairs
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)

# Starting with an Empty Dictionary
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 4
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# Modifying Values in a Dictionary
# alien_0['color'] = 'yellow'

# print(alien_0['color'])

# Removing Key-Value Pairs
# del alien_0['points']

# print(alien_0)

# A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(favorite_languages)

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}")

# Using get() to Access Values
# print(favorite_languages['belal'])
print(favorite_languages.get('belal', 'Value does not exist'))
print(favorite_languages.get('sarah'))