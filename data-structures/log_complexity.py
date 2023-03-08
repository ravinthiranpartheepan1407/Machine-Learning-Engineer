input = int(input("Enter a number: ")) #O(1)
input_data = [1,2,3,4,5,6] #O(1)

def main(append):
    for i in range(input): #O(n) -> Same input so it will have same notation
        for j in range(input): #O(n) -> Same input so it will have same notation
            print(i, j) #O(1)

main(input_data) #O(1)

print("The complexity will be: O(n^2) and it has poor complexity")
