"""

# Write a function that takes in a non-empty array of integers that are
# sorted in ascending order and returns a new array of the dsame length 
# with the squares of the original integers also sorted in ascending order

Example: 

        sample input = [1,2,3,5,6,8,9]
        output: [1,4,9,25,36,64,81]

"""



def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [0 for _ in array]

    smallerValueIndex = 0
    largerValueIndex = len(array) - 1
    current = largerValueIndex
    while smallerValueIndex <= largerValueIndex:
        if abs(array[smallerValueIndex]) < abs(array[largerValueIndex]):
            sortedSquares[current] = array[largerValueIndex] * array[largerValueIndex]
            largerValueIndex -= 1
        else:
            sortedSquares[current] = array[smallerValueIndex] * array[smallerValueIndex]
            smallerValueIndex += 1
        current -= 1
    return sortedSquares

sortedSquaredArray([1, 2, 3, 5, 6, 8, 9])