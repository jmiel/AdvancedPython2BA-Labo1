# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import math 
def fact(n):
    if n<0:
        raise ValueError
    result=1
    while n>0:
        result *=n
        n -=1
    return result


def roots(a, b, c):
    delta=(b**2) - (4*a*c)
    if delta < 0:
        return None
    if delta == 0:
        return (-b/(2*a),)
    else:
        return ((-b+math.sqrt(delta))/(2*a), (-b-math.sqrt(delta))/(2*a))
    
def f(x):
    return x
def integrate(function, lower, upper):
    return (function (lower)+function (upper))* (upper - lower) / 2 #first degree approximation

if __name__ == '__main__':
    print(fact(5))
    print(roots(2, 1, -1))
    print(integrate(f, -1, 1))
