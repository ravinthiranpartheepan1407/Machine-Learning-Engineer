# Set is an unordered collection of unique object and it accepts only VALUES
# Use SET keyword to convert list to SET
# Set can return

user = {
    "Ravi",
    "Suren",
    "Ethan",
    "Hunt"
}

password = {
    "Ravi",
    "Value",
    "Suren",
    "007"
}

user.add("Ethan")
user.add("Hunt")
print(user)

my_user = [1,2,3,4,5]
convert = set(my_user)
convert.add(2)
convert.add(6)
print(convert)

print(1 in convert)


# Methods

# Differnce: Return the elements that are not common in the sets
print(user.difference(password))

# Discard: Remove an element from a set if it is a member.
user.discard(password)
print(user)

# Difference_update: Remove all elements of another set from this set.
user.difference_update(password)
print(user)

# Intersection: Returns common element from both sets; Can also use A & B to find out INTERSECTIONS
print(user.intersection(password))

# Disjoint: Will return TRUE if there is no single common elements present in both SETS
print(user.isdisjoint(password))

# Unions: Combines both SETS and Rejects duplicates; Can also use A | B to find out UNIONS
print(user.union(password))
print (user | password)

# Is_Subset: if entire SET A matches SET B then it return true otherwise false
print(user.issubset(password))

# Is_Superset: if SET B matches the entire SET A then it return true otherwise false
print(password.issuperset(user))
