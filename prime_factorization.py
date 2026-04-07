#functions that returns the prime factors of a number 

def prime_factors(num):
    
    #two numbers that multiply to get the user entered number 
    factors = []
    i = 2 
    while i * i <= num:
        if num % i == 0:
            factors.append(i)
            num //= i 

        else:
            i += 1

    if num > 1:
        factors.append(num)
    return factors

user_num = int(input("Enter a number: \n"))
print(f"The prime factors of {user_num} are :{prime_factors(user_num)}")




    
