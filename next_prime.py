#program that generates the next prime number until the user chooses to stop asking for the next one
def my_prime(num):
    
    if num <= 1:
        return False
    
    i = 2 
    while i * i <=num:
        if num % i == 0:
            return False
        i +=1

    return True

def next_prime(n):
    next_num = n + 1
    while True :
        if my_prime(next_num):
            return next_num
        next_num += 1

try:
    user_input = int(input("Enter a number to find the next prime number:\n"))
    next_prime_number = next_prime(user_input)
    print(f"The next prime number after {user_input} is : {next_prime_number}")

except ValueError:
    print("Invalid input please enter an integer")

            
    
    



