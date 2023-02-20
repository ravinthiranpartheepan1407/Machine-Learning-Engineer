is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("Atleast you are getting there")
else:
    print("You need magic powers")

# False
print(True is 1)
# False because each list stored in different memory
print([] is [])
# False because ASCII is different for a and A
print('a' == 'A')