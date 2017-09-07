
file=raw_input("input file name?")

print"We are going to erase file %r"%file

print"If you don't wan't that hit CTRL+C"

print "If you do want that hit RETURN"

raw_input("?")

print "opening the file.."

target=open(file,'w')

print"truncating the file.."

target.truncate()

print "Now I am going to ask you for three lines"

lineone=raw_input("line one?")
linetwo=raw_input("line two?")
linethree=raw_input("line three?")

print "I am going to write these to file"

target.write(lineone)
target.write("\n")
target.write(linetwo)
target.write("\n")
target.write(linethree)
target.write("\n")

print "And finally we close"
target.close()


