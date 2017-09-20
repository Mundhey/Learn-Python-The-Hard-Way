def somefuncion(rohan,sohan):
    i=0
    numbers=[]
    for i in range(0,rohan,sohan):
        print "at the top i is %d" % i
        numbers.append(i)
        i = i + sohan
        print"numers now", numbers
        print "at the bottom number is %d" % i

    print "The numbers"

    for abc in numbers:
        print abc



somefuncion(67,5)





