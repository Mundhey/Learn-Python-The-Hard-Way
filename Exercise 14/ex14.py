from sys import argv

script,urr_name=argv

prompt='>'

print "Hi %s i am %s script"%(urr_name,script)
print"I'd like to ask you a few question's"
print "do you ike ma %s?"%urr_name
like=raw_input(prompt)
print "where do you live %s"%urr_name
live=raw_input(prompt)
print "what kind of computer do you have"
computer=raw_input(prompt)

print """
alright, so you said %r about liking me
you live in %r . not sure where that is
and you have a %r computer.Nice
"""%(like,live,computer)

