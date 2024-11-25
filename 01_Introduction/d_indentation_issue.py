"""
Purpose: Importance of Indentation

"""

print("Hello World 1")
# print("Hello World 2") # IndentationError: unexpected Indent
print("Hello World 2")
print("Hello World 3")

# block code - if, else, elif, for, while, def, class
# if 12>13:
# print("12 is greater than 13")
# IndentationError: expected an Indent block after 'if' statement

if 12>13:
    print("12 is greater than 13")

if 12>13:
    print("greater")
else:
    print("It is lesser")

if 1<2:
    print("case 1")
elif 2>1:
    print("case 2")
else:
    print("case 3")


i=0
while i<10:
    j=0
    while j<10:
        print(i, "*", j, "=", i*j)
        j+=1
    print()
    i+=1

def my_func():
    return "hello world"

class Myclass:
    def __init__(self):
        pass

#tabs vs white-space
#PEP 8(Python Enhancement Proposal) - Code style guide
# Prefer white-spaces, to tabs; four white-spaces
