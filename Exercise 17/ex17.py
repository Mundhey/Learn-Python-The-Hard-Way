from os.path import exists

from_file=raw_input("form file?")
to_file=raw_input("to_file?")

print "Copying from %r to %r"%(from_file,to_file)

#we could do these two one line too ,how?

in_file=open(from_file)
in_data=in_file.read()

print "The input file is %d bytes long"%len(in_data)

print "does the output file exise? %r"%exists(to_file)

print "hit return to continue"

raw_input()

out_file=open(to_file,'w')
out_file.write(in_data)

print "Allright , everything is done"

out_file.close()
in_file.close()