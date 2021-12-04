"""
LeetCode 72:

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

                Insert a character
                Delete a character
                Replace a character

Example 1:
        
            Input: word1 = "horse", word2 = "ros"
            Output: 3
            Explanation: 
            horse -> rorse (replace 'h' with 'r')
            rorse -> rose (remove 'r')
            rose -> ros (remove 'e')
        
Example 2:

            Input: word1 = "intention", word2 = "execution"
            Output: 5
            Explanation: 
            intention -> inention (remove 't')
            inention -> enention (replace 'i' with 'e')
            enention -> exention (replace 'n' with 'x')
            exention -> exection (replace 'n' with 'c')
            exection -> execution (insert 'u')

Solution:

            CASE 1: WORD1[i] == WORD2[j]
                        DP_Table[i][j] = DP_Table[i-1][j-1]
            
            CASE 2: WORD1[i] != WORD2[j]

                    CASE 2A: Delete ith element in WORD1, then i is same as i-1 and j remains same
                                DP_Table[i][j] = DP_Table[i-1][j]
                    CASE 2B: Replace ith element in WORD1 by jth element of WORD2, then 
                                DP_Table[i][j] = DP_Table[i-1][j-1]
                    CASE 2C: Insert jth element in WORD2 at ith element of WORD1
                                DP_Table[i][j] = DP_Table[i][j-1]

Dynamic Programming Table:

                  ''    W   O   R   D   2
            
            ''    0     1   2   3   4   5    

            W     1     

            O     2

            R     3

            D     4

            1     5

           
"""
import time

class levenshtein_distance():

    def __init__(self,s1,s2):
        #construct the table
        self.row = len(s1)+1
        self.column = len(s2)+1
        self.str1 = s1
        self.str2 = s2
        self.levenshteinTable = [[0] * self.column for _ in range(self.row)]
        


    def levenshtein_distance(self,method):
        if method == 'd':
            return self.levenshtein_distance_dynamic_programing()
        elif method == 'r':
            dp = [[-1] * self.column for _ in range(self.row)]
            return self.levenshtein_distance_recursion(dp,0,0)


    def levenshtein_distance_recursion(self,dp,index1,index2):


        if index1 == self.row-1:
            return  len(self.str2) - index2 
        if index2 == self.column -1:
            return len(self.str2) -index1
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        if self.str1[index1] == self.str2[index2]:
            return self.levenshtein_distance_recursion(dp,index1+1,index2+1)
        else:
            dp[index1][index2] =  1 + min (self.levenshtein_distance_recursion(dp,index1+1,index2+1),
                                            self.levenshtein_distance_recursion(dp,index1+1,index2),
                                            self.levenshtein_distance_recursion(dp,index1,index2+1))
            
        return dp[index1][index2]
    
    def levenshtein_distance_dynamic_programing(self):

        for i in range(self.row):
            self.levenshteinTable[i][0] = i
        
        for i in range(self.column):
            self.levenshteinTable[0][i] = i

        for i in range(1,self.row):
            for j in range(1,self.column):
                if self.str1[i-1] == self.str2[j-1]:
                    self.levenshteinTable[i][j] = self.levenshteinTable[i-1][j-1]
                else:
                    self.levenshteinTable[i][j] = 1 + min(
                        self.levenshteinTable[i-1][j-1],
                        self.levenshteinTable[i-1][j],
                        self.levenshteinTable[i][j-1]
                    )
        return self.levenshteinTable[self.row-1][self.column-1]

levenshtein = levenshtein_distance("xabc","abcxy")
tic =time.time()
print(levenshtein.levenshtein_distance('d'))
print(f'Time taken by Dynamic programing is {(time.time() - tic)*1000}')

tic =time.time()
print(levenshtein.levenshtein_distance('r'))
print(f'Time taken by Recursion with Memoization is {(time.time() - tic)*1000}')
