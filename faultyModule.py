'''
A faulty module to demonstrate the use of importlib.reload()
'''

def computePi():
    '''Compute pi/4 using arctan() Taylor series and print Pi on std output'''
    n = 1
    sign = 1
    while n < 1000000:
        p += sign/n
        sign *= -1
        n += 2
    print(4*p)