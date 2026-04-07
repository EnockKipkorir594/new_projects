#generating fibonacci sequence using iterative method 
def fib_sequence_iterative(n):
    if n <= 0 :
        return []
    elif n == 1:
        return [0]
    else:
        series =  [0,1]
    while len(series) < n:
        next_term = series[-1] + series[-2]#adds the last number to the second last 
        series.append(next_term)
    return series
    
fib_num = 10 
my_fib = fib_sequence_iterative(fib_num)
print(f"The fibonacci sequence for {fib_num} is {my_fib}")



#generating fibonacci sequence using recursive method 

def fibo_recursive(n):
    if n <= 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)
    #adds the last number to the second last
def fibo_series_recursive(n):
    series = []
    for i in range(n):
        series.append(fibo_recursive(i))
    return series

next_term = 10
fib_seq = fibo_series_recursive(next_term)
print(f"fibonacci seuence for {next_term} terms is : {fib_seq}")

#generate fibonacci sequence using memoization method 

from functools import lru_cache

@lru_cache (maxsize=None)
def fib_memo(n):
    if n <= 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fib_memo(n-1) + fib_memo(n-2)
    #adds the last number to the second last
def fib_memo_series(n):
    series = []
    for i in  range(n):
        series.append(fib_memo(i))

    return series
next_term = 10
fib_se = fib_memo_series(next_term)
print(f"fibonacci sequence to {next_term} terms is :{fib_se}")

#generates the fibonacci sequence using a generator 

def fib_generator(n):
    a, b = 0, 1
    count = 0 
    while count < n:
        yield a
        a, b = b, a+b
        count += 1

next_term = 10
fib_gen = list(fib_generator(next_term))
print(f"fibonacci sequence to {next_term} terms is : {fib_gen}")




    
