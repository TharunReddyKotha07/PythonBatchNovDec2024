#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
"""
temperature = input("Enter the temperature in C or F to convert: ")
if temperature[-1].lower() == 'c':
    out_temp =  (int(temperature[:-1]) * (9/5)) + 32
    print(temperature[:-1],"°C = ", out_temp,"°F")

elif temperature[-1].lower()  == 'f':
    out_temp = (int(temperature[:-1]) - 32) * 5/9
    print(temperature[:-1],"°F = ", out_temp,"°C")
