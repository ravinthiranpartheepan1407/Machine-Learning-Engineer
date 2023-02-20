# Truthy and Falsy can be processed with bool type
# Truthy must contains 1, some or some values
# Falsy contains 0s, None and no values

# Ternary Opeartor: ( Message ? condition 1 : condition 2)

is_user = bool("Ravi")
is_pass = bool("Suren")
is_auth = bool("")

if is_user and is_pass and is_auth:
    print("User Allowed")
elif is_auth:
    print("User Not Authenticated but provided username and password")
else:
    print("User not allowed")

is_following = bool("Following")
can_communicate = "Communication Allowed" if is_following else "Communcation Not Allowed"
print(can_communicate)