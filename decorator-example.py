from time import time
recipe_name = str(input("Enter food name: "))
def cook_food(receipe):
    def pack_food(recipe_name):
        start_time = time()
        cooked = receipe(recipe_name)
        packed_time = time()
        print(f'Duration for cooking {recipe_name} and Packing {recipe_name}: {packed_time - start_time}')
    return pack_food

@cook_food
def order_food(data):
    print(data)
    for i in range(1000): # Starts from 0 and finsih at 1000
        i*5

order_food(recipe_name)