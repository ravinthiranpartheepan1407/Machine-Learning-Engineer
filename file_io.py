# file = open("./WhenTo.txt")
# print(file.read())
# print(file.seek(2))
# print(file.readlines(4))

# Automatically set the mode to 'r' -> read
# 'w' -> write
# 'r+' -> read and write : The cursor will write from zero (0) index in the text file
# '_a_' -> append to the line
# '_w_' -> Write to a file : Write to a new file


with open("./food.txt", mode='w') as file_open:
    text = file_open.write("Welcome Food Bar")
    print(text)

# with open("./food.txt", mode='a') as file_open:
#     text = file_open.write(": Idly")
#     print(text)

try:
    with open("./food.txt", mode='r') as file_read:
        print(file_read.readlines())
except:
    raise FileNotFoundError("File Not Found Dude!")
