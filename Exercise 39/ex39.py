#create a mapping of state to abreveation

states={
'oregon' : 'or',
'florida' : 'fl',
'california' : 'ca',
'new york' : 'ny',
'michigan' : 'mi'
}

cities={
'ca':'san francisco',
'mi':'detroit',
'fl':'jacksonville'

}

print states
print  cities

#add some more cities
cities['ny']='new york'
cities['or']='portland'

#print out some cities
print '-'*20
print "michigan abbreveation is",states['michigan']
print "florida abbreveation is",states['florida']

#print out some cities

print '-'*20
print "ny state has",cities['ny']
print "or state has",cities['or']

#do it by using state then cities dict

print "-"*20
print "michigan has",cities[ states['michigan']]
print "florida has",cities[states['florida']]

#print every state abbreaviation
print '-'*20
for state,abbrev in states.items():
    print "%s is abbreaveated is %s"%(state,abbrev)

#every city in state

print '-'*20
for abbrev,city in cities.items():
    print"%s has city %s"%(abbrev,city)

# now do both at the same time
print '- ' * 10
for state, abbrev in states.items():
 print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])


# safely get an abbreviation by state that might not be there
print '- ' * 10
state = states.get('Texas', None)


if not state:
    print "Sorry, no Texas."


# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
