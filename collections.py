# Counter is used to count number of elements in a list
# Default_dict : Takes first argument as a default value or callable function(Lambda, anonymous, method) and secord argument as dict

from collections import Counter, defaultdict, OrderedDict

food = ["Idly", "Dosa", "Pongal", "Idly"]
print(Counter(food))

food_dict_lambda = lambda: 5
def food_dict_lambda_func():
        return 7

food_dict = defaultdict(food_dict_lambda_func, {
    'Idly': 10,
    'Dosa': 20,
    'Pongal': 20
})

print(food_dict['Vada'])

