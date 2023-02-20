# Tuples are like list but it is immutable.. Overall. it's an immutable list
# Tuples use () syntax where list use [] syntax
user = {
    (1,2): [10, 50, 27],
    ("data"): "Bat File"
}

user.update({"data": "Spiderman"})

print(user[(1,2)])
print(user["data"])
