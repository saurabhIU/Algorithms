def search_triplets(arr):
  triplets = []
  # TODO: Write your code here
  arr.sort()
  for i in range(len(arr)):
    current_element = arr[i]
    if i > 0 and current_element == arr[i-1]:
        continue

    left = i+1
    right = len(arr)-1
    while left < right:
        local_sum = arr[left] + arr[right] + current_element
        if local_sum == 0:
          triplets.append([current_element,arr[left],arr[right]])
          left+=1
          right-=1
        elif local_sum < 0:
          left+=1
        else:
          right-=1

    return triplets


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
