# sha_1: FIPS (Federal Information Processing Standards) created these secure hashing algorithms for hashing data.
# sha_224
# sha_256
# sha_384
# sha_512
# blake_2b
# blake_2s

# Note: Hash and Digest are Interchangable
# Make sure the hashing algorithms are FIPS compliant otherwise don't use

from hashlib import sha1,sha224,sha256
import hashlib

# UTF-8 encoding used to translated uni chars to strings

# hash_file_list = ["./pdf/food.pdf", "./pdf/watermarked_pdf.pd"]

data = str(input("Enter data to hash: "))

def sha_1_hashing(data) -> str :
    hash_data = sha1(data.encode('utf-8')).hexdigest()
    # return str(hash_data)
    print(f'The Blak2b hash is {hash_data}')

def sha_224_hashing(data) -> str : 
    hash_data = sha224(data.encode('utf-8')).hexdigest()
    print(f'The Blak2b hash is {hash_data}')

def sha_256_hashing(data):
    hash_func = sha256()
    update_data = str(input("Update your data: "))
    hash_data = sha256(data.encode('utf-8')).hexdigest()
    update_hash = hash_func.update(update_data.encode('utf-8'))
    digest_updated_hash = hash_func.hexdigest()
    print(hash_data)
    print("The updated hash for data 256 is: ", digest_updated_hash)

def sha256_hash_pdf():
    with open("./pdf/food.pdf", mode='rb') as file:
        digest = hashlib.sha256(file.read()).hexdigest()
        save_digest = bytes(digest.encode('utf-8'))
        with open("./pdf/hashed_pdf.pdf", mode="wb") as hashed_file:
            hashed_file.write(save_digest)
        print(f'The file hash is: {digest}')


def blake2_hash_data(data):
    hash = hashlib.blake2b(data.encode('utf-8')).hexdigest()
    print(f'The Blak2b hash is {hash}')

sha_1_hashing(data)
sha_224_hashing(data)
sha_256_hashing(data)
sha256_hash_pdf()
blake2_hash_data(data)
