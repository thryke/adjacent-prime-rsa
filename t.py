import math
import sys
import decimal
import gmpy2

# n - large number that is the product of two adjacent prime numbers
# e - some number 1<e<phi(n) that is coprime with phi(n)
# c - ciphertext
# test -  python3 t.py 1189541400606115059081659849771032347306378800607141166155176122451 65537 299604539773691895576847697095098784338054746292313044353582078965
D = decimal.Decimal
n = D(sys.argv[1])
e = D(sys.argv[2])
c = D(sys.argv[3])

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def computePQ(N):
	start = math.floor(D(N).sqrt())
	q = gmpy2.next_prime(start)
	p = N/q
	return p, q

def computePhi(p, q):
	phi = (p-1)*(q-1)
	return phi

def decrypt(ct, d, n):
	pt = pow(ct, int(d), n)
	print(str(pt))	

def main():
	p, q = computePQ(n)
	phi = computePhi(p, q)
	gcd, a, b = egcd(e, phi)
	d = a
	decrypt(c, d, n)

if __name__ == "__main__":
    main()
