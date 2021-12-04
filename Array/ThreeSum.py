
# Problem: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Input: nums = []
# Output: []

# Input: nums = [0]
# Output: []


def threeNumberSum(array, targetSum):
    array.sort()
    output = []
    for i in range(len(array)):
        left_ptr = i+1
        right_ptr = len(array)-1

        while left_ptr < right_ptr:
            temp_sum = array[left_ptr] + array[right_ptr] + array[i]
            
            if temp_sum == targetSum:
                output.append([array[i],array[left_ptr],array[right_ptr]])
                left_ptr +=1
                right_ptr -= 1
            elif temp_sum < targetSum:
                left_ptr +=1
            else:
                right_ptr -= 1
                
    return output




input = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(input, targetSum))