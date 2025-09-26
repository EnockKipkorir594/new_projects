#functions that returns the prime factors of a number 

def prime_factors(num):
    
    #two numbers that multiply to get the user entered number 
    factors = []
    divisor = 2 
    while divisor * divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor 

        else:
            divisor += 1

    if num > 1:
        factors.append(num)
    return factors

user_num = int(input("Enter a number: \n"))
print(f"The prime factors of {user_num} are :{prime_factors(user_num)}")




    
