def add(a,b):
    print"Adding %d + %d"%(a,b)
    return a+b

def subtract(a,b):
    print "Subtracting %d - %d"%(a,b)
    return a-b

def multiply(a,b):
    print "multiplying %d * %d" % (a, b)
    return a*b

def divide(a,b):
    print "Dividing %d / %d" % (a, b)
    return (a/b)

print "let's do some math just with functions"

age=add(30,5)
height=subtract(45,5)
weight=multiply(5,5)
iq=divide(100,2)

print "age %d height %d weight %d iq %d"%(age,height,weight,iq)

#puzzle

what=add(age,subtract(height,multiply(weight,divide(iq,2))))

print "that becomes",what,"can you do it by hand?"