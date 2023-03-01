# r' -> Represents Raw String
# \b: used to match a word character and non-word character
# (?:{0}) -> used to group a tuple/list and assigns the element we want to insert to the palceholder part {0} 
# {0} -> is a placeholder; 
# (?:placeholder) -> used to group a word from a tuple, list
# format('|'.join(keyword) -> used to insert the (list,tuple) into the placeholder {0}

import re

search = input("Search Positions here: ")
keyword = ['deisgner', 'developer', 'devops', 'product']

# Search Menu Functionality
compile_kw = re.compile(r'\b(?:{0})\b'.format('|'.join(keyword)))
search_position = compile_kw.match(search)
print(search_position)
