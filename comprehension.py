# Comprehension used to specify list, tuples, dict in a single line

my_family = ["son", "daughter", "dad", "mom"]
tuple_family = tuple(my_family)
dict_family = {
    "hierarchy1": 50,
    "hierarchy2": 49,
}

iterate_family = {key:values/2 for key, values in dict_family.items()}
print(list(zip(iterate_family.values(), my_family)))
print(tuple_family)