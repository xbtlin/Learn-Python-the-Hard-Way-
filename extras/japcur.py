from sys import *

adelta,bdelta,a2,b2 = argv[1:]

adelta=float(adelta)
bdelta=float(bdelta)
a2=float(a2)
b2=float(b2)

a1=a2/(1+adelta)

b1=b2/(1+bdelta)

c1=a1/b1
c2=a2/b2

jcur=(c2-c1)/c1

print jcur

print (1+0.0028)/(1-0.0034)-1