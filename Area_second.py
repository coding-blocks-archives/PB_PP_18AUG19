import math
pi = math.pi

def square(x):
    return x**2

def rectangle(l,b):
    return l*b

def circle(r):
    return pi*r**2

if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]
    shape = arguments[0]
    if shape == 'circle':
        print(circle(int(arguments[1])))
    elif shape == 'rectangle':
        a = int(arguments[1])
        b = int(arguments[2])
        print('Area of rectangle:', rectangle(a,b))
    elif shape == 'square':
        print(square(int(arguments[1])))
    else:
        print('This option is not available.')



