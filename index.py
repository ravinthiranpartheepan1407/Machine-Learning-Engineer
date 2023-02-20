#   Data types: -> # int, float, bool, list, tuples, set, dict, str

#   Classes: -> Which will be our own Custom Types

#   Specialized Data types: -> Whenever we don't have the datatype we want then we can use modules (Specialized data types)

#   None: -> Nothing

print(type(20 + 1.1))
print(9.0 + 1.0)

print(5**2)

user_name = input("Enter your user name:" + " ")
user_password = input("Enter your password:" + " ")
enter_code = input("Enter code:" + " ")
hashed_pass = '*' * int(len(user_password))


print(f'User: {user_name} with password: {hashed_pass} along with code: {enter_code}')