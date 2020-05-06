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
n = D(sys.argv[1])
print(n)
def decrypt(nVal):
    with decimal.localcontext() as ctx:
        ctx.prec = 2000
        start = math.floor(n.sqrt())
        print('start = ', start)
    q = gmpy2.next_prime(start) # finding the first prime immediately following the root of N
    p = nVal/q 			# computing p through the divison of n by q because we know p and q are adjacent
    print('p =',int(p))
    print('q =',q)

def main():
    decrypt(n)

if __name__ == "__main__":
	main()
