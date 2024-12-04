#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithm:
============
1) is it empty 
2) is it alphabet 
3) is it vowel or not 

NOTE: handle case-sensitivity 
"""

VOWELS = ['a', 'e', 'i', 'o', 'u']

ip_chr = input("Enter any character between a-z|A-Z) ").strip().lower()

if ip_chr:
        if ip_chr.isalpha():
                if ip_chr in VOWELS:
                      print("Input character is a VOWEL")
                else:
                        print("Input character is not a VOWEL")
        else:
                print("Given input is not a character")
else:
        print("Given an empty input")
