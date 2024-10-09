import os

def clear():
    os.system('cls')

def header(h1, h2, h3):
    print(".: Calculator :.")
    print("-" * 14)
    print("-", h1)
    print("-", h2)
    print("-", h3)
    print("-" * 14)
    print("add | Add two numbers")
    print("sub | Subtract two numbers")
    print("mul | Multiply two numbers")
    print("div | Divide two numbers")
    print("-" * 14)