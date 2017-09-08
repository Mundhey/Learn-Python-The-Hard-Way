input_file=raw_input("input file name?")

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)


def print_a_line(line_count,f):
    print line_count,f.readline(),

input_file=open(input_file,'r')

print"let us first print the whole file\n"

print_all(input_file)

print "let's now rewind kind of a tape"

rewind(input_file)

print "let's print three lines"

current_line=1

print_a_line(current_line,input_file)

current_line=current_line+1

print_a_line(current_line,input_file)

current_line=current_line+1

print_a_line(current_line,input_file)



