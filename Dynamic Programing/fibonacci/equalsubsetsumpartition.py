def can_partition(num):
    sum_of_array = sum(num)
    if sum_of_array % 2 != 0:
        return False
    return can_partition_helper(num,sum_of_array/2,0)


def can_partition_helper(num,target,index):
    if index == len(num) :
        return 0
    
    if num[index] == target:
        return num[index]
    
    if num[index] < target:
        sum = num[index] + can_partition_helper(num,target-num[index],index+1)
        if sum == target:
            return sum

    return can_partition_helper(num,target,index+1)


    

    

print(can_partition([1,2,3,4]))
print(can_partition([1,1,3,4,7]))