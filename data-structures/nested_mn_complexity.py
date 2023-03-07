# The nested loops complexity will be: 

value = int(input("Enter a value: ")) #O(1)
value_append = [] #O(1)
list = [10,20,30,40,50,60,70,80] #O(1)

def main():
    try:
        for i in list: #O(m)
            if i > value: #O(n)
                value_append.append(i) #O(1)
                # break
            else: #O(1)
                print("Values out of range")
        
        print("The Enter value is:", value) #O(1)

    except:
        raise ValueError("Please enter a number dude!")
    

main()
print("The appended values are: ", value_append)
print("Overall complexity is: O(m*n)")