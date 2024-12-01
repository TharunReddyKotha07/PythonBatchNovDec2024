"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

"""
# Initial Principal Balance
initial_principal_balance = float(input("Enter the Initial Principal Balance: "))

# Annual interest rate
annual_interest_rate = float(input("Enter the Annaual Intrest Rate: "))
annual_interest_rate = annual_interest_rate / 100 

# Time in years
time_in_years = float(input("Enter the time (in years): "))

# Computing the simple interest
simple_interest = (initial_principal_balance * annual_interest_rate * time_in_years) + initial_principal_balance

compound_interest = initial_principal_balance * ((1 + annual_interest_rate / 12)**(12*time_in_years))


print("Simple Interest: ", simple_interest)
print("Compound Interest: ", compound_interest)










# Assignment
# 1. Compound Interest Calculation
#     ref: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php