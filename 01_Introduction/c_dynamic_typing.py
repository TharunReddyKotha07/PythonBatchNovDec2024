"""
Purpose: Python is a dynamic Typed Language.
    Programming Languages
        - Classification
            1. Static-Typed Languages
                - first declare the variables, &
                - then use them
                    int a, float b  # Declaration
                    a=10            # initiation

            2. Dynamic Typed Languages
                - create when you need. No declaration needed
                    num1 = 123
                -line or block based execution

    python code -> python byte code -> pythonInterpreter -> c compiler -> machine
    so, python is slower compared to compiler based languages
"""

num1=100
type(num1)

print(type(num1))

print(num1)
print("num1")

print("num1", num1)
print("num1 =", num1, "type =", type(num1))

# works in both static and dynamic-typed language
num1=300
print("num1 =", num1, "type =", type(num1))

# Python is dynamic-typed language
num1=300.0
print("num1 =", num1, "type =", type(num1)) # float

num1=300.
print("num1 =", num1, "type =", type(num1)) # float

num1=300,
print("num1 =", num1, "type =", type(num1)) # tuple

num1=(300,)
print("num1 =", num1, "type =", type(num1)) # tuple

num1=-0.09
print("num1 =", num1, "type =", type(num1)) # float

num1=0.09j
print("num1 =", num1, "type =", type(num1)) #complex

num1="300"
print("num1 =", num1, "type =", type(num1)) # string

num1="three"
print("num1 =", num1, "type =", type(num1)) # string

num1=True
print("num1 =", num1, "type =", type(num1)) # Boolean
#num1 = true # python is a case sensitive language

num1=False
print("num1 =", num1, "type =", type(num1)) # bool

num1=None
print("num1 =", num1, "type =", type(num1)) # None

num1="NONE"
print("num1 =", num1, "type =", type(num1)) # string

num1="none"
print("num1 =", num1, "type =", type(num1)) # string

#NOTE: Strings need to be declared in quotes