def kadanesAlgorithm(array):
    global_max = array[0]
    current_max = array[0]
    start_index = 0
    end_index = 0
    for i in range(1,len(array)):
        # If current array item is max till current index the this index
        # should be reset the start position of max contiguous sub array
        # and current_max should be equal to the current array index value
        if max(array[i],current_max+array[i]) == array[i]:
            start_index = i
            current_max = array[i]
        else:
            current_max = current_max+array[i]
        # If current_max is greater than global max then update global max
        # and also update end_index of contiguous sub array
        if current_max > global_max:
            global_max = current_max
            end_index = i
        
    return start_index,end_index,global_max

v = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
start_index , end_index , value = kadanesAlgorithm(v)
print(f"Sum of largest subarray = {value} ,end_index = {end_index} and starting index = {start_index}")

