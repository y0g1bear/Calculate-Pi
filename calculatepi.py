"""
calculatepi.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Write and submit a Python program that computes an approximate value of π by calculating the following sum:

(see: https://github.com/HHS-IntroProgramming/Calculate-Pi/blob/master/README.md)

This sum approaches the true value of π as n approaches ∞.

Your program must ask the user how many terms to use in the estimate of π, how many decimal places, 
then print the estimate using that many decimal places. Exactly like this:

I will estimate pi. How many terms should I use? 100
How many decimal places should I use in the result? 7
The approximate value of pi is 3.1315929


Note: remember that the printed value of pi will be an estimate!

"""
#import math
n = int(input("I will estimate e. How many terms should I use? "))
decimals = int(input("How many decimal places should I use in the result? "))
e = 4*sum([((-1.0)**k)/math.factorial(2*int(k)) for k in range(0,n)])
print("The approximate value of e is {0}".format(round(e, decimals)))
print("(The true value of e is {0})".format(round(math.e, decimals)))
