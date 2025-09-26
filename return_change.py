def change_returner():
  
    cost = float(input("Enter the cost in : \n"))
    money_given = float(input("Enter the money given in : \n"))
    if money_given < cost :
        print("You have provided insufficient funds")
        return 
    
    change_cents = (money_given - cost) * 100
    
    
    quarters = change_cents // 25
    change_cents %= 25

    dimes = change_cents // 10
    change_cents %= 10

    nickels = change_cents // 5 
    change_cents %= 5

    pennies = change_cents


    print(f"You change is {quarters} quarters , {dimes} dimes, {nickels} nickels and {pennies} pennies")

change = change_returner()
print(change)
    
       



