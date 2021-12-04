# Dynamic Programing approach
def longest_common_subsequence(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    
    dynamic_table = [[0 for i in range(l2+1)] for j in range(l1+1)]

    
    """
    Youtube Link: https://www.youtube.com/watch?v=ASoaQq66foQ

    Formula for Dynamic table

                  ""    a   b   d   f
            
            ""     0    0   0   0   0

            c      0

            a      0

            r      0

            b      0

        dynamic_table[i][j] =   1 + dynamic_table[i-1][j-1]                                 #if s1[i] = s2[j]
                                max(dynamic_table[i-1][j] , dynamic_table[i][j-1])          #if s1[i] != s2[j]

    """

    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if s1[i-1] == s2[j-1]:
                dynamic_table[i][j] = dynamic_table[i-1][j-1] + 1
            else:
                dynamic_table[i][j] = max(dynamic_table[i-1][j], dynamic_table[i][j-1])
    

    """
     Construct the common sub-sequence:

            [  [0, 0, 0, 0], 
               [0, 1, 1, 1], 
               [0, 1, 1, 1], 
               [0, 1, 2, 2], 
               [0, 1, 2, 2], 
               [0, 1, 2, 3]
            ]

    """
    
    i = l1
    j = l2
    output = []
    while (i >=1 and j >=1):
        if s1[i-1] == s2[j-1]:
            output.append(s1[i-1])
            i -= 1
            j -= 1
        else:
            if dynamic_table[i-1][j] >= dynamic_table[i][j-1]:
                i -= 1
            else:
                j -= 1
    return output[::-1]

def longest_common_subsequence_recursion(s1,s2):
    cache = [[-1]*len(s2) for _ in range(len(s1))]
    return longest_common_subsequence_recursion_helper(cache,s1,s2,0,0)


def longest_common_subsequence_recursion_helper(cache,s1,s2,index1,index2):

    #Base condition
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if cache[index1][index2] != -1:
        return cache[index1][index2]
    if s1[index1] == s2[index2]:
        return 1 + longest_common_subsequence_recursion_helper(cache,s1,s2,index1+1,index2+1)
    else:
        c1 = longest_common_subsequence_recursion_helper(cache,s1,s2,index1+1,index2)
        c2 = longest_common_subsequence_recursion_helper(cache,s1,s2,index1,index2+1)
        cache[index1][index2] = max(c1,c2)
    
    return cache[index1][index2]



text1 = "HIEROGLYPHOLOGY"
text2 = "MICHAELANGELO" 
#output = 3 and ["a,c,e"]

print(longest_common_subsequence(text1,text2))
print(longest_common_subsequence_recursion(text1,text2))


    