# Given two non-empty array of integers, write a function that determines whether the
# second array is a subsequence of first one
# A subsequence of an array is a set of numbers that aren't necessarily the adjacent in the array
# but are in the same order as they appear in the array. For example array [1,3,4]  form a sub-sequence
# of the array [1,2,3,4]

def isValidSubsequence(array, sequence):
    # Write your code here.
    array_index = seq_index = 0
    while array_index < len(array) and seq_index < len(sequence):
        if array[array_index] == sequence[seq_index]:
            seq_index += 1
        array_index += 1
    return seq_index == len(sequence)


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]))
