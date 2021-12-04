"""
Problem Statement:

Given two integer arrays to represent weights and profits of ‘N’ items, 
we need to find a subset of these items which will give us maximum 
profit such that their cumulative weight is not more than a given number ‘C’.
Write a function that returns the maximum profit. Each item can only be
selected once, which means either we put an item in the knapsack or skip it.

EXAMPLE:

      PROFIT = [1, 6, 10, 16]
      WEIGHT  = [1, 2, 3, 5]
      CAPACITY = 6

      Table[i][j] = Optimal solution for a knapsack with capacity j using items 1 to i.

      If j < W[i] then:
            Table[i][j] = Table[i-1][j]
      else:
            Table[i][j] = Max[( P[i] + Table[i-1][j-W[i]]), Table[i-1][j])

                              c   a   p   a   c   i   t   y
                  
                P     W       0   1   2   3   4   5    6
 
                0     0       0   0   0   0   0   0    0 

                1     1       0    

                6     2       0
                
                10    3       0  

                16    5       0
        
        Backtracking:

              1. Go to last item in the DP Table
              2. Compoare it with last row same column.
              3. If its different then that means, that item is included in the solution
              4. Go to previous row and column column - W[row]
              5. continue till row 1
                  

"""


import time
def solve_knapsack(profits, weights, capacity,algo):
  
  if algo == 'm':
    cache = [[-1 for i in range(capacity+1)] for j in range(len(profits))]
    return solve_knapsack_helper_memo(profits, weights, capacity, 0,cache)
  elif algo == 'r':
    return solve_knapsack_helper(profits, weights, capacity, 0)
  elif algo == 't':
    dp = [[0 for j in range(capacity+1)] for i in range(len(weights))]
    for i in range(capacity+1):
      if weights[0] <= i:
        dp[0][i] = profits[0]
    return solve_knapsack_helper_matrix(profits, weights, capacity,dp)
  else:
    return f'Incorrect algo type'  

  
# Solution 1: Recursive solution

def solve_knapsack_helper(profits, weights, capacity,current_index):

  if current_index >= len(profits) or capacity <= 0:
    return 0
  

  if capacity >= weights[current_index]:
    return max(profits[current_index]+solve_knapsack_helper(profits, weights,capacity-weights[current_index],current_index+1),
                 solve_knapsack_helper(profits, weights,capacity,current_index+1))
   
  else:
    return solve_knapsack_helper(profits, weights,capacity,current_index+1)

# Solution 2: Recursive solution with memoization

def solve_knapsack_helper_memo(profits, weights, capacity,current_index,cache):

  if current_index >= len(profits) or capacity <= 0:
    return 0
  
  if cache[current_index][capacity] != -1:
    return cache[current_index][capacity]
  
  profit1 = 0
  if capacity >= weights[current_index]:
    profit1 = profits[current_index]+solve_knapsack_helper_memo(profits, weights,capacity-weights[current_index],current_index+1,cache)

  profit2 = solve_knapsack_helper_memo(profits, weights,capacity,current_index+1,cache)
  cache[current_index][capacity] = max(profit1,profit2)
  return cache[current_index][capacity]
  

#Solution 3: Bottom-up DP method

def solve_knapsack_helper_matrix(profits, weights, capacity,cache):

  for i in range(1,len(weights)):
    for j in range(1,capacity+1):
      if weights[i] <= j:
        cache[i][j] = max(cache[i-1][j], profits[i] + cache[i-1][j-weights[i]])
      else:
        cache[i][j]  = cache[i-1][j]
  return cache[len(profits)-1][capacity]

#Solution 4: weight and profit are given in an array together. Return max profit and
# list of indices that makes maximum profit

def knapsackProblem(items, capacity):
  values = [[0 for j in range(capacity+1)] for i in range(len(items)+1)]
  result = []
  for i in range(1,len(items)+1):
    currentweight = items[i-1][1]
    currentprofit = items[i-1][0]
    for j in range(1,capacity+1):
      if currentweight <= j:
        profit1 = values[i-1][j-currentweight] + currentprofit
        profit2 = values[i-1][j]
        values[i][j] = max(profit1,profit2)
      else:
        values[i][j] = values[i-1][j]

# Now get all the indices that make maximum profit

  result.append(values[len(items)][capacity])

  j = capacity
  indexes = []
  for i in range(len(items),0,-1):
    if values[i][j] != values[i-1][j]:
      indexes.append(i-1)
      j = j-items[i-1][1]
  result.append(indexes)
  return result



tic = time.time()
print(f'Maximum profit via bruteforce recursion method is is {solve_knapsack([6, 1, 10, 16], [1, 2, 3, 5], 7,"r")} and time taken is {(time.time()-tic)*1000}')
tic = time.time()
print(f'Maximum profit via memoized recursion method is is {solve_knapsack([6, 1, 10, 16], [1, 2, 3, 5], 7,"m")} and time taken is {(time.time()-tic)*1000}')
tic = time.time()
print(f'Maximum profit via bottom up method is is {solve_knapsack([6, 1, 10, 16], [1, 2, 3, 5], 7,"t")} and time taken is {(time.time()-tic)*1000}')

tic = time.time()
print(f'Maximum profit via bruteforce recursion method is is {solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6,"r")} and time taken is {(time.time()-tic)*1000}')
tic = time.time()
print(f'Maximum profit via memoized recursion method is is {solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6,"m")} and time taken is {(time.time()-tic)*1000}')
print(knapsackProblem([
  [1, 1],
  [6, 2],
  [10, 3],
  [16, 5]
],7))
