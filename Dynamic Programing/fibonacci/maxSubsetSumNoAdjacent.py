# Time complexity is O(N) and space complexity is O(1)
# We use dynamic programing in this problem where we keep
# track of last two sums and calculate largest sum till 
# current index as current index largest sum = max of previous sum and 
# sum of current element and previous to previous sum
# max_sum_till_current_index = max(element[i]+element-i-2, element[i-1])
def maxSubsetSumNoAdjacent(array):

    if len(array) == 0:
        return -1
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return max(array[0],array[1])

    
    first_index_sum = array[0]
    second_index_sum = array[1]
    global_max  = max(first_index_sum,second_index_sum)
    for i in range(2,len(array)):
        max_sum = max(second_index_sum,first_index_sum+array[i])
        first_index_sum = second_index_sum
        second_index_sum = max_sum
        if max_sum > global_max:
            global_max = max_sum
    return global_max

array = [1, -1, 6, -4, 2, 2]
print(maxSubsetSumNoAdjacent(array))

