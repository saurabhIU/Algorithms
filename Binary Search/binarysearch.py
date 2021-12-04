def binarySearch(array, target):
    # Write your code here.
    start = 0
    end = len(array)-1
    return binarysearchrecursive(array,start,end,target), binarysearchiterative(array,start,end,target)


# Time complexity is O(logN) and space complexity is O(logN) as recursive call stacks take space

def binarysearchrecursive(array,start,end,target):
    if end >= start:
        mid = start + (end-start) // 2
        
        if array[mid] == target:
            return mid
    
        elif array[mid] > target:
            return binarysearchrecursive(array,start,mid-1,target)
        else:
            return binarysearchrecursive(array,mid+1,end,target)
    else:
        return -1

# Time complexity is O(logN) and space complexity is O(1) as recursive call stacks take space

def binarysearchiterative(array,start,end,target):
    while start <= end:

        mid = start + (end-start) // 2
        
        if array[mid] == target:
            return mid
    
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return -1




array = [0,1,21,33,45,45,61,71,72,73]
target =33

print(binarySearch(array,target))