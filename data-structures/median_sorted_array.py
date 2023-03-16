# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Breakdown:

# 1. Merge both arrays
# 2. iterate thorugh the merged_array using without for loop with time complexity of O(1) if not merged then it would be O(log(m+n))
# 3. Sum the numbers and store it to a variable
# 4. Divide the sum by using len function of the merged list

list_1 = [1,3,7]
list_2 = [2]

# Time complexity with: O(1)
def merge_list_median(list_1, list_2):
    merged_list = list_1 + list_2
    print(sorted(merged_list))
    cal_median = len(merged_list)  
    merge_sum = sum(merged_list)
    median = merge_sum/cal_median
    print(median)
       

# Time complexity with: O(log(m+n))
def merge_median_log(list_1, list_2):
    for i in list_1:
        sort = sorted(i)
        print(s)

merge_list_median(list_1, list_2)
