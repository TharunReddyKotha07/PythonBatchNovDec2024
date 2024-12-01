#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable
Step 2: create a reverse string , from the given string, using string reversal
Step 3: compare both with a condition and decide

"""

test_string = input("Enter any string:")
print("test_string    :", test_string)

test_string1 = test_string.replace(" ", "")


# reverse string
reverse_string = test_string[::-1]
print("reverse_string :", reverse_string)

reverse_string1 = test_string1[::-1]

print(test_string == reverse_string)

print("test_string == reverse_string:", test_string == reverse_string)


if test_string == reverse_string:
    print(test_string, "is palindrome")
else:
    print(test_string, "is NOT a palindrome")    

if test_string1 == reverse_string1:
    print(test_string1, "is palindrome sentence")
else:
    print(test_string1, "is NOT a palindrome sentence")  

# Assignment: test if a given sentence is palindrome or not
# HINT: ignore the whitespace and check