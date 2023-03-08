input_1 = ['Ravi', 'Suren', 'Kohli']
input_2 = ['Sachin', 'Smith', 'Starc']

append_1 = []
append_2 = []

append_mn = []

class MplusN:
    def main_1(self, input_1, input_2):
        for i in input_1:
            append_1.append(i)
            
        for j in input_2:
            append_2.append(j)


class MdotN:
    def main_2(self, input_1, input_2):
        for i in input_1:
            for j in input_2:
                dict_mn = {'Batting': i, 'Bowling': j}
                append_mn.append(dict_mn)

obj_1 = MplusN()
obj_2 = MdotN()

obj_1.main_1(input_1, input_2)
obj_2.main_2(input_1, input_2)

print(append_1)
print(append_2)
print(append_mn)

