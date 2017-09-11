print " let's practice everything"

print "you\'d need to know \' bout escapes with \\ that dp \n newlines and \t tabs"

poem ="""
\tThe lovely family
with logic so firmly planted
cannot discern \n the needs of love
\n\t nor comprehend passion from intuition
"""

print"--------"

print poem

print "------"

five=10-2+3-6

print"this should be five %d "%five

def secret_formula(started):
    jellybeans=started*5000
    jars=jellybeans/1000
    crates=jars/100
    return jellybeans,jars,crates

start_point=10000

beans,jars,crates=secret_formula(start_point)

print " with a starting point of %d "%start_point

print "we'd have %d beans , %d jars and %d crates "%(beans,jars,crates)

start_point=start_point/20

print "we can also do that this way"

print "we'd have %d beans , %d jars and %d crates "% secret_formula(start_point)



