import math
def mulinv(k):
    r1, r2, t1, t2 =26,k,0,1
    while r1 != 1:
        if r2 ==0:
            break
        q=r1//r2
        r=r1%r2
        t = t1-(t2*q)
        r1=r2
        r2=r
        t1=t2
        t2=t
    if t1>0:
        return t1
    else:
        return t2+t1

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p


def coprime(x):
    prime = [i for i in range(5,x)]
    for i in prime:
        g =gcd(x,i)
        if g == 1:
            # print(i)
            return i

def key_gen(n,p,q):
    phi = (p-1)*(q-1)
    e = coprime(phi)
    for i in range(phi):
        if (i*e)%phi == 1:
            d=i
            break
    return e,d

def rsa_encrypt(m,e,n):
    return (pow(m,e)%n)

def rsa_decrypt(m,d,n):
    return (pow(m,d)%n)

def RSA():
    p,q = map(int,input("Enter p and q: ").split(" "))
    n=p*q
    e,d =key_gen(n,p,q)
    m = int(input("Enter the message(number) to encrypt: "))
    c = rsa_encrypt(m,e,n)
    p = rsa_decrypt(c,d,n)
    print("Public Key: (",n,e,")\nPrivate Key: (",n,d,")\n")
    print("Encrypted Text:",c)
    print("Decrypted Text:",p)

RSA()             
