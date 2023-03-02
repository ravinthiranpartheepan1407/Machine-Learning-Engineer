num_A = int(input("Enter a number for Label A: "))
num_B = int(input("Enter a number for Label B: "))
class add_value:
    def value(self, num_A, num_B):
        return num_A + num_B + 5
    def total_value(self, num_A, num_B):
        total = num_A + num_B + 7
        return total

class subtract_value:
    def total_values(self, num_A, num_B):
        return num_A - num_B


obj = add_value()
sub = subtract_value()
print(sub.total_values(num_A, num_B))
print(obj.total_value(num_A, num_B))
print(obj.value(num_A, num_B))
