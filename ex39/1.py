states = {
     'Oregon':  'OR',
     'Florida': 'FL',
     'Califorrnia': 'CA',
     'New York': 'NY',
     'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' *10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbv is: ", states['Michigan']
print "Florida's abbv is: ", states['Florida']

print '-' *10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print "_" *10
for state, abbrev in states.items():
    print "%s is abbreviated %s" %(state, abbrev)


print '_' *10
for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)

for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s " %(state, abbrev, cities[abbrev])


print '_' *10

state = states.get('Oregon')
print state

state = states.get('Texas', None)
if not state:
    print "sorry, no Texas."

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" %city
