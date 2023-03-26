# This is for rsa challenges that provide all the info, or at least just missing n.
# n can be figured out by p*q.
# If you don't have p and q, then use https://github.com/Ganapati/RsaCtfTool

from Crypto.Util.number import inverse, long_to_bytes

c, n, e, q, p = 0, 0, 0, 0, 0
# c is encrypted message
# n is magic number. p*q should equal n
# e will most likely be 65537 for most ctfs
# p and q are prime factors of n

print("\nPlease enter values for RSA problem. If there is no value, just press enter.\n")
c = int(input("c: ") or 0)
n = int(input("n: ") or 0)
e = int(input("e: ") or 0)
p = int(input("p: ") or 0)
q = int(input("q: ") or 0)
print("\n")

if c == 0:
    print("Please provide info for c...")
    exit()
if (n == 0) and ((p != 0) and (q != 0)):
    n = p*q
if e == 0:
    print("Please provide info for e...")
    exit()
if p == 0 or q == 0:
    print("Missing value for p, q, or both. May need to use RsaCtfTool...")
    exit()
   
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,n)
print(long_to_bytes(m).decode('utf-8'))

