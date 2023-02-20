from functools import reduce
my_pets = ['Tom','Jerry','Tim','Dorothy']
first_strings = ['T','J','T','D']
cat_rank = [1,4,3,2]
scores = [67,47,87,97]

# Caps
for caps in range(len(my_pets)):
    my_pets[caps] = my_pets[caps].capitalize()
print(my_pets)

# Sort Numbers and convert to tuples
merge = tuple(zip(first_strings, sorted(cat_rank)))
print(merge)

# Filter Score greater than 50
def filter_score():
    for i in scores:
        if i > 50:
            print(i)
filter_score()

def combine(cat_rank, scores):
    return cat_rank + scores

print(tuple(reduce(cat_rank, scores)))
