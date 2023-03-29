# You are given an integer array nums. 
# You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. 
# Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

# Return the maximum number of points you can earn by applying the above operation some number of times.

# Breakdown:

# 1. Create an earn input var with type of int
# 2. Create point_system with type of int
# 3. Iterate through the point_system
# 4. val_points = points[0] + points[1]....points[n] + points[n]
# 5. Check if the val_points[n] == earn print the points earned else insufficient request

points_to_earn = int(input("Enter your point value: "))
point_pool = [2,7,8,1,3,3,6]
your_points = []
def earn_n_delete(points_to_earn, point_pool):
    for values in range(1,len(point_pool)):
        # print(point_pool[values])
        val_points = point_pool[values] + point_pool[values-1]
        print(f'The points index: {point_pool[values]} + {point_pool[values-1]} = {val_points}')
        if points_to_earn == val_points and points_to_earn > 2:
            your_points.append(val_points)
            point_pool.remove(point_pool[values])
            point_pool.remove(point_pool[values-1])
            break
        else:
            print("Insufficient point earning request")
        
        # elif points_to_earn in point_pool:
        #     your_points.append(points_to_earn)
        #     point_pool.remove(point_pool[values])
        #     break

earn_n_delete(points_to_earn, point_pool)
print(f'Your current points are: {your_points}')
print(f'The available points in the pool are: {point_pool}')