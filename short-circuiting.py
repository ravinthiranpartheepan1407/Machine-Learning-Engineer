# Short Circuiting can be used when we use OR operator

is_friend = bool("Friend")
is_known = True

if is_friend or is_known:
    print("Best Friend")
else:
    print("Not my friend")