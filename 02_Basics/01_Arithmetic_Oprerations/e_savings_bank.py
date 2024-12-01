"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

# Creating a variable balance with an initial value of 0
balance = 0
print("Initial balance", balance)

# Adding Initial Deposit of 1500
balance += 1500
print("Balance after Initial Deposit", balance)

# Salary credited of 3300
balance += 3300
print("Balance after Salary Credit", balance)

# Online Purchase of 33.33
balance -= 33.33
print("Balance after Online Purchase", balance)

# House Rent paid of 1500
balance -= 1500
print("Balance after paying rent", balance)

# Displaying the final balance
print("Final Balance:", balance)
