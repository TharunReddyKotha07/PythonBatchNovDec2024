"""
Purpose: Grocery Store

    Item       cost
    ------------------------
    rice        10/kg
    wheat       34/kg

Algorithm
---------
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items from the user(in run time)

NOTE: input()
        -> to get value in run-time
        -> will give any input as string only

"""

# cost of items
cost_of_rice = 10  # per kg
cost_of_wheat = 34  # per kg


# Quantities of Items
qty_of_rice = input("Enter Qty. of Rice  (in Kgs):")
# qty_of_rice = int(qty_of_rice)
qty_of_rice = float(qty_of_rice)
print("Qty of Rice  :", qty_of_rice, type(qty_of_rice))



# qty_of_wheat = input('Enter Qty. of Wheat(in Kgs):')
# qty_of_wheat = float(qty_of_wheat)

qty_of_wheat = float(input("Enter Qty. of Wheat(in Kgs):"))


# Selling Price Computation
sp_of_rice = cost_of_rice * qty_of_rice
print("SP of Rice   :", sp_of_rice)

sp_of_wheat = cost_of_wheat * qty_of_wheat
print("SP of Wheat  :", sp_of_wheat)


total_sp = sp_of_rice + sp_of_wheat
print("Total SP     :", total_sp)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------

from datetime import datetime
current_time = datetime.now()


Cashier = "cashier"
LINE_SPACE = 90
HALF_LINE_SPACE = 45
ONE_THIRD_SPACE = 30


print(LINE_SPACE * '*')
print()
print("Walmart".center(LINE_SPACE))
print("Lorem ipsum 258".center(LINE_SPACE))
print("City Index - 02025".center(LINE_SPACE))
print("RECEIPT".center(LINE_SPACE, "-"))
print()
print(LINE_SPACE * '*')
print(Cashier.ljust(HALF_LINE_SPACE) + current_time.strftime(current_time.strftime("%Y-%m-%d %H:%M:%S")).rjust(HALF_LINE_SPACE))
print(LINE_SPACE * '-')
print()
print(("ITEM").ljust(ONE_THIRD_SPACE) + ("Quantity").center(ONE_THIRD_SPACE) + ("PRICE").rjust(ONE_THIRD_SPACE))
print()
print(("RICE").ljust(ONE_THIRD_SPACE) + (str(qty_of_rice) + "kg").center(ONE_THIRD_SPACE) + ("$"+str(sp_of_rice)).rjust(ONE_THIRD_SPACE))
print(("WHEAT").ljust(ONE_THIRD_SPACE) + (str(qty_of_wheat) + "kg").center(ONE_THIRD_SPACE) + ("$"+str(sp_of_wheat)).rjust(ONE_THIRD_SPACE))
print(LINE_SPACE * '-')
print(LINE_SPACE * '-')
print(("TOTAL AMOUNT").ljust(HALF_LINE_SPACE) + ("$"+str(total_sp)).rjust(HALF_LINE_SPACE))
print(("CASH").ljust(HALF_LINE_SPACE) + ("$"+str(total_sp)).rjust(HALF_LINE_SPACE))
print(("CHANGE").ljust(HALF_LINE_SPACE) + ("$0").rjust(HALF_LINE_SPACE))
print()
print(LINE_SPACE * '-')
print()
print("THANK YOU!!".center(LINE_SPACE, "*"))
print()
print()