# Looping Through a Dictionary
user_0 = {
    'username': 'belalbh',
    'first': 'belal',
    'last': 'hossain',
}
# Looping Through All Key-Value Pairs
# for key , value in user_0.items():
#     print(f"Key: {key}")
#     print(f"Value: {value}")
#     print()

# Looping Through All the Keys in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# Looping Through a Dictionary’s Keys in a Particular Order
# for name in sorted(favorite_languages.keys()):
#     print(name.title())

# Looping Through All Values in a Dictionary
for language in favorite_languages.values():
    print(language.title())