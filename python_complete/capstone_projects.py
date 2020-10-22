from math import pi
from math import e

def pi_to_n(n):
    print(n*pi)
    return n*pi

def e_to_n(n):
    print(n*e)
    return n*e

def fibonacci(a,b,n):
    sequence = [a,b]
    for i in range(n):
        b += a
        a = sequence[-1]
        sequence.append(b)
    return sequence

# fibonacci(1,1,10)
# pi_to_n(10)
# e_to_n(10)
