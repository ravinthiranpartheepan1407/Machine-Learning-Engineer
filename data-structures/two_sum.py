# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Breakdown:

# 1. Add numbers to num list
# 2. Implement a for loop to iter through the list -> O(n)
# 3. Add key and value in enumarate type of the list (Only value)
# 4. use Target and Value to perform math ops
# 5. If the pair is new then append to the dict else ignore it

# target = int(input("Enter Target Number: "))
nums = [6,4,3,2,5]
target = int(input("Enter a Target: "))

def sum_eq_target(nums, target):
	pairs = {} # Dict declare
	for key, value in enumerate(nums): # key = 0 and value = 0
		add = target - value # 9 - value(nums[0]) => 9-6 = 3 and 3 will be inserted in dict
		if add in pairs: # if 3 is alread in dict and 6 is already in dict then it's a pair
			# target = 9; value = enum(num[2]) => 9-3 = 6 => 6 is already in dict
			print(pairs[add], key)
		pairs[value] = key

def sub_eq_target(nums, target):
	sub_pairs = {}
	for key, value in enumerate(nums):
		sub = value-target
		if sub in sub_pairs:
			print(sub_pairs[sub], key)
		sub_pairs[value] = key
		
def mul_eq_target(nums, target):
	mul_pairs = {}
	for key, value in enumerate(nums):
		mul = target-value
		print(mul)
		if mul in mul_pairs:
			print(mul_pairs[mul], key)
		mul_pairs[value] = key
		print(mul_pairs[value])

def div_eq_target(num, target):
	div_pairs = {}
	for key, value in enumerate(nums):
		div = target * value
		print(div)
		if div in div_pairs:
			print(div_pairs[div], key)
		div_pairs[value] = key

div_eq_target(nums, target)
mul_eq_target(nums, target)
sub_eq_target(nums, target)
sum_eq_target(nums, target)
