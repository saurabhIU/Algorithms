import time
def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memoization(n):
    mem = [-1 for x in range(n+1)]
    return fibonacci_memoization_helper(mem,n)

def fibonacci_memoization_helper(mem,n):
    if n<2:
        return n
    
    if mem[n]>=0:
        return mem[n]
    
    mem[n]=fibonacci_memoization_helper(mem,n-1)+fibonacci_memoization_helper(mem,n-2)

    return mem[n]

def fibonacci_tabular(n):
  dp = [0, 1]
  for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])

  return dp[n]

    


tic = time.time()
n = 40

print(f'{n}th fibonacci is {fibonacci(n)} and time taken is {(time.time()-tic)*1000}')
tic = time.time()
print(f'{n}th fibonacci via memoization is {fibonacci_memoization(n)} and time taken is {(time.time()-tic)*1000}')
tic = time.time()
print(f'{n}th fibonacci via memoization is {fibonacci_tabular(n)} and time taken is {(time.time()-tic)*1000}')