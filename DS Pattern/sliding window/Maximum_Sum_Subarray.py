"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].


Solution:


If you observe closely, you will realize that to calculate the sum of a contiguous subarray, we can utilize the sum of the previous subarray. For this, consider each subarray as a Sliding Window of size ‘k.’ To calculate the sum of the next subarray, we need to slide the window ahead by one element. So to slide the window forward and calculate the sum of the new position of the sliding window, we need to do two things:

Subtract the element going out of the sliding window, i.e., subtract the first element of the window.
Add the new element getting included in the sliding window, i.e., the element coming right after the end of the window.


"""

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  max_sum , window_sum = 0,0
  current_index = 0

  for i in range(len(arr)-k+1):
    window_sum += arr[i]

    if i >= k:
      max_sum = max(max_sum,window_sum)
      window_sum -= arr[current_index]
      current_index += 1
  return max_sum


print(f"Maximum sum of a subarray of size K: {max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])}")
print(f"Maximum sum of a subarray of size K: {max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])}")