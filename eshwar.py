import math
p=3
q=7
n=p*q
print("n=",n)
phi=(p-1)*(q-1)
print("phi=",phi)
e=2
while(e<phi):
    if(math.gcd(e,phi)==1):
        break
    else:
        e+=1
print("e=",e)
k=2
d=((k*phi)+1)/e
print("d=",d)
print("public key",{e,n})
print("private key",{d,n})
msg=11
print("original message",msg)
C=pow(msg,e)
C=math.fmod(C,n)
print("encrypted message",C)
M=pow(C,d)
M=math.fmod(M,n)
print("decrypted msg",M)
