# Insert, Append, Extends, Pop, Remove, Clear

# Insert requires index and value; It doesn't return any value
data = ["Hello", "My", "Name", "is"]
new_data = data.insert(4, "Suren")
print(data)

# Append required only value and add it to the end of the current list; It doesn't return any value
new_append = data.append("Ravi")
print(data)

# Extends adds the value to end of the current list; It doesn't return any value
new_extends = data.extend(["Arkhamm"])
print(data)

# Pop removes the last element and it can return a value
new_pop = data.pop(-1)
print(new_pop)

# Remove the specified element; It doen't return any value
new_remove = data.remove("Ravi")
print(data)

# Clears all the element; It doesn't return any value
new_clear = data.clear()
print(data)