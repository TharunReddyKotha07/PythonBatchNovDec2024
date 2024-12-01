"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results
"""
# getting the feet value  
height_in_feet = float(input("Enter the height in Ft:"))

# computing height in cms 
height_in_cms  = height_in_feet * 12 * 2.54
height_in_inches = height_in_feet * 12

# Displaying the final reult
print("Height in feet:", height_in_feet)
print("Height in Inches:", height_in_inches)
print("Height in cms:", height_in_cms)