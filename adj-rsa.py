import os
import json
import sys
import time
import decimal
import math
import gmpy2
import numpy as np
from Crypto.PublicKey import RSA

D = decimal.Decimal
#n = D(sys.argv[1])
n = D(94614493)
e = 65537
c = 2996

print(n)
def decrypt(N, e, c):
    with decimal.localcontext() as ctx:
        ctx.prec = 2000
        start = math.floor(N.sqrt())
        print('start = ', start)
    q = gmpy2.next_prime(start) # finding the first prime immediately following the root of N
    p = N/q 			# computing p through the divison of n by q because we know p and q are adjacent
    print('p =',int(p))
    print('q =',q)
    phi = (p-1)*(q-1)
    print('phi =',phi)
    d = modinv(e, phi)
    print('d =',int(d))
    m = (c**d)%N
    print(m)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse doesn\'t exist')
    else:
        return x % m

def main():
    decrypt(n, e, c)

if __name__ == "__main__":
	main()
