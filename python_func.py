def f(x):
    return x%2!=0 and x%3!=0
l = filter(f,range(2,25))
l2 = range(1,10)
def add(x,y):
    return x+y
l3 = reduce(add, range(1, 11), 20)
print (lambda x:x*2)(3)
print "Hhj"
print l