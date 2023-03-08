input_1 = ['Ravi', 'Suren', 'Kohli'] #O(1)
input_2 = ['Sachin', 'Smith', 'Starc'] #O(1)

append_1 = [] #O(1)
append_2 = [] #O(1)

append_mn = [] #O(1)

class MplusN:
    def main_1(self, input_1, input_2): #O(1)
        for i in input_1: #O(m)
            append_1.append(i)
            
        for j in input_2: #O(n)
            append_2.append(j)
    print('The complexity for this op is: O(m+n) because It has different notation')


class MdotN:
    def main_2(self, input_1, input_2):
        for i in input_1: #O(m)
            for j in input_2: #O(n)
                dict_mn = {'Batting': i, 'Bowling': j}
                append_mn.append(dict_mn)
    print('The complexity for this op is: O(m*n) because It has different notation and nested structure')

obj_1 = MplusN() #O(1)
obj_2 = MdotN() #O(1)

obj_1.main_1(input_1, input_2) #O(1)
obj_2.main_2(input_1, input_2) #O(1)

print(append_1)
print(append_2)
print(append_mn)

