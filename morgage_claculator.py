#pogram to calculate the monthly payments of a fixed time morgage given nth terms at a given interest

def calc_morgage(loan_amount, annual_interest, loan_term_years):
    if loan_amount <= 0 or annual_interest <= 0 or loan_term_years <= 0 :
        print("Error : incorrect input")
        return None 
     
    monthly_interest = annual_interest / 12
    number_of_payments = loan_term_years * 12

    #calculate the morgage using amortization formula 
    numerator = monthly_interest * (1 + monthly_interest) ** number_of_payments
    denominator = (1 + monthly_interest) ** number_of_payments - 1

    monthly_payment = loan_amount * (numerator/ denominator)
    if denominator == 9:
        return loan_amount / number_of_payments
    return monthly_payment

loan_amount = 20000
annual_interest = 0.5
loan_term_years = 7




    


     