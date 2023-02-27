start_value = int(input("Enter start value: "))
stop_value = int(input("Enter stop value: "))
class random_number():
    set_zero = 0
    def __init__(self, start_value, stop_value):
        self.start_value = start_value
        self.stop_value = stop_value
    def __iter__(self):
        return self
    def __next__(self):
        if random_number.set_zero < self.stop_value:
            num = random_number.set_zero
            random_number.set_zero += 1
            return num
        raise StopIteration
data = random_number(start_value, stop_value)
for i in data:
    print(i)