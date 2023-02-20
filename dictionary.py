# Dictionary is an unordered key-value pair and it's the element in the memory through keys.

# Simple dictionary
simple_dict = {
    'Bond': '007',
    'Hitman': 'Agent 47',
    'Ethan': 'MI6'
}

print(simple_dict['Bond'])

# Creating a list and integrate dictionary inside the list
spy_list = [
    {
        'Bond': ['007', 'No Time To Die', 'Spectre'],
        'Hitman': 'Agent 47',
        'Ethan': 'MI6'
    },
    {
        'James': ['007', 'Spectre'],
        'Hitman 47': 'Agent 47',
        'Hunt': 'MI6'
    }
]

print(spy_list[0]['Bond'][1])
print(spy_list[1]['James'][:])