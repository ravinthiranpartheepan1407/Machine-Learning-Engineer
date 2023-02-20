# Ordered sequence of an object
# A list can contains any data types

# Data structures: Used to store and organize a info.

# List are mutable

data = ["Suren", "Ravi", "Data", "Science"]
print(data[1])

shopping_cart = ["Games CD", "Board Games", "Playstation"]
select_item = input("Enter the index to pick an item" + " ")
print(f'The select item is {shopping_cart[int(select_item)]}')

mutate_item = shopping_cart.append(input("Enter New Product" + " "))
print(shopping_cart)
print(f'Select the newly added product {shopping_cart[-1]}')