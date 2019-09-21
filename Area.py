import sys

pi = 3.14
def square(a):
    return a**2

def circle(r):
    return pi* r**2

def rectangle(l,b):
    return l*b

print('Module is running!!')

print(sys.argv)

print('name is:', __name__ )
