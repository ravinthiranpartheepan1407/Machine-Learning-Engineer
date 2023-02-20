# Use "Get" for object methods

user = dict(name="Suren", age=55)
print(user)

user_data = {
    "username": "Suren",
    "Password": "Pass"
}
print(user_data["Password"])
print(user_data.get("Password"))

username = input("Enter Your Username:")
typed_user = dict(name = username)
print(typed_user)

print('Ravi' in typed_user)
print('Password' in user_data)

# Fetch by keys, values, items, update

print("username" in user_data.keys())
print("Pass" in user_data.values())
print(user_data.items())
print(f'The updated password is: {user_data.update({"Password": typed_user.get("name")})}')
