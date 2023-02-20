# While used to iterate until the condition is met
# Use BREAK keyword to escape once the condition is met; otherwise it will keep looping
# If you didn't use BREAK then you can use ELSE; if you use BREAK then ELSE won't work

# BREAK can also be used in for loop

# CONTINUE used to trace back to the condition until the condition is met; 
# PASS used to break over to next statement

i = 0
while i < 50:
    print(i)
    i = i+1
    break

# When to use WHILE: Not sure about the element / objects that you want to iterate then use WHILE
# When to use FOR: Iterating over iteratable objects

while True:
    response = input("Say Something: ")
    if response == "bye":
        break

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# Iterate over picture
# if 0 -> " " and 1 -> "*"
# End used to specify if you want a new or in a single line

for item in picture:
    for pixel in item:
        if pixel == 1:
            print("*", end="")
        else:
            print("0", end="")
    print("")

