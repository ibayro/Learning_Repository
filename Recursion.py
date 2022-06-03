"""
Recursion Functions

1. Hello (n) Times
2. Sum          0+1+2+3+4+5
3. Factorial    5! = 1*2*3*4*5 = 120
4. Fibonacci    0,1,1,2,3,4,5,,8,13,21,34,55,89
"""


def hello(x):
    if x == 0:
        return
    else:
        print("Hello")
        hello(x-1)


hello(2)


def sum(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)


y = sum(5)
print("Total sum according to input is " + str(y))


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


print("Total factorial sum based on input is " + str(factorial(5)))


def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


print("Total fibonacci sum according to your input is " + str(fibonacci(10)))