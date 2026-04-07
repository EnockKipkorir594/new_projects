#Find PI to the nth number 
#using Chudnovsky algorithm
from decimal import Decimal, getcontext
import math 

def calc_pi(n):
    getcontext().prec = n + 5# n+5 increases the accuracy of pi 

    C = 426880 * Decimal(math.sqrt(10005))
    M =1
    L = 13591409
    X = 1
    K = 6
    S = L
    for i in range(1, n):
        M = (M * (K ** 3 - 16*K)) // (i ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L)/ X
        K += 12
    pi = C / S

    getcontext().prec = n 

    return + pi 

p = int(input("Enter number of decimal places: \n"))

pi_val = calc_pi(p)
print(f"Pi to {p} decimal places: \n {pi_val}")








