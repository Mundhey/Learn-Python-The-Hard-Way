ten_things="Apples Oranges Crows Telephone Light Sugar"
print"Wait ther's not ten things in taht list lets fix this"

stuff=ten_things.split(' ')

print stuff
more_stuff=["day","night","song","frisbe","corn","banana","girl","boy"]

print len(stuff)

while(len(stuff)!=10):
    next_one=more_stuff.pop()
    print "Adding",next_one
    stuff.append(next_one)
    print "There's %d items now"%len(stuff)

print "there we go",stuff

print "let's do some things to stuff"

print stuff[2]

print stuff[-2]

print stuff.pop()

print '**'.join(stuff)
