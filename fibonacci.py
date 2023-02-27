value = int(input("Enter Range: "))

# Using Class
class fibonaaci():
   def gen(value):
      start = 0
      stop_store = 1
      for i in range(value):
        yield start
        temp = start
        start = stop_store
        stop_store = temp + stop_store

iterate = fibonaaci.gen(value)
for x in iterate:
   print(x)

# Using List
fibonaaci_list = [0, 1]
appened_fibonnaci = []

def fibonacci_using_list(value):
   fibonaaci_list_start = fibonaaci_list[0]
   fibonaaci_list_stop = fibonaaci_list[1]
   for i in range(value):
      yield fibonaaci_list_start
      temp = fibonaaci_list_start #temp = 0; 
      fibonaaci_list_start = fibonaaci_list_stop #fib_lis_start = 1
      fibonaaci_list_stop = temp + fibonaaci_list_start #fib-lis_stop = 0 + 1 -> 1
      
      # Iter 2 Breakdown
      # temp = 1; fib_lis_start = 1; fib_lis_stop = 1 + 1 = 2

      #Iter 3 Breakdown
      # temp = 1; fib_list_start = 2; fib_lis_stop = 1 + 2 = 3

for x in fibonacci_using_list(value):
   appened_fibonnaci.append(x)
   print(appened_fibonnaci)
  



        

        
    