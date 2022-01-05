def remove_duplicates(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1

if __name__ == '__main__':
    arr = [0,0,1,1,1,2,2]
    print(remove_duplicates(arr))