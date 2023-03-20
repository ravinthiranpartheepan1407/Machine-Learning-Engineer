# Hash Tables are useful in DB, caches, and other more important use cases

# Hash a key using SHA-256 (FIPS) algorithm and store the value. Fetch the value from the hashed key

# Breakdown:

# 1. Create an input variables for key and value
# 2. Create an empty for mapping the key and value pair
# 3. Import SHA-256 and encode it with the input
# 4. Update the key hash to value field in the dict

from hashlib import sha256
from random import randint

id = str(input("Enter an Account ID: "))
password = str(input("Enter a Account value: "))

cust_db = [] # 

def hash_maps(id, password): # O(n)
    gen_account_id = randint(0,20) # Start and Stop
    encode_password = sha256(password.encode('utf-8')).hexdigest()
    store_pair = {
        'Id': id,
        '_Account_ID': gen_account_id, # Private Field -> Hash field using randint
        'password': encode_password # Hash field using sha256
    }
    
    cust_db.append(store_pair)
    print(cust_db)

hash_maps(id, password)

# Dict: Used for storing unique values and used for storing infinite no.of records also immutable
# Using list nested inside a dict will allow the fields to mutate since the lists are mutable 
# For ex: {key: [mutable], value: immutable without list}

acc_id = input("Enter customer ID: ")
def get_custid(acc_id): # O(n)
    for items in range(len(cust_db)): # Size == len(cust_DB) -> For this example the size will be 1 as there is only one record exists
        get_accID = cust_db[items].get('_Account_ID')        
        if int(acc_id) == int(get_accID):
            print("Customer Found in our DB")
        else:
            print("Customer Not Found in our DB")


get_custid(acc_id)

# Update a hash let's say password field
update_pass = str(input("Enter your new password: "))
def update_hash(update_pass):
    for items in range(len(cust_db)):
        get_accID = cust_db[items].get('_Account_ID')
        if int(acc_id) == int(get_accID):
            hash = sha256(update_pass.encode('utf-8')).hexdigest()
            update_pair = {
                'password': hash # Hash field using sha256
            }
            cust_db[items]['password'] = update_pair
            print(f'Updation Successful: {cust_db}')
        else:
            print("Unauthorized Access!")

update_hash(update_pass)
            



