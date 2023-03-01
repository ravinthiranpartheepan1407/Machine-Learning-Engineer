import re
# reg_list = (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]./[a-zA-Z0-9-.]+$)
append_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password_regex = re.compile(r"[A-Za-z0-9$#%@]{8,}\d")
email = input("Enter Your Email: ")
password = input("Enter Password: ")
validate_email = append_regex.search(email)
validate_password = password_regex.match(password)
print(validate_email)
print(validate_password)

