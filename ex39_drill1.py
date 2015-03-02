# create states with bundeslaender
states = {
	'Baden-Wuertemberg': 'BW',
	'Bayern': 'BY',
	'Brandenburg': 'BB',
	'Hessen': 'HE',
	'Niedersachsen': 'NI',
	'Nordrhein-Westfalen': 'NW',
	'Mecklenburg-Vorpommern': 'MV',
	'Rheinland-Pfalz': 'RP',
	'Saarland': 'SL',
	'Sachsen': 'SN',
	'Sachsen-Anhalt': 'ST',
	'Schleswig-Holstein': 'SH',
	'Thueringen': 'TH'
}

# add city states
states['Hamburg'] = 'HH'
states['Bremen'] = 'HB'
states['Berlin'] = 'BE'

# create state-city mapping
cities = {
	'BY': 'Muenchen',
	'HE': 'Wiessbaden',
	'SL': 'Saarbruecken',
	'BW': 'Stuttgart'
}

# print out some cities
print '-' * 10
print "BW has: ", cities['BW']
print "BY has: ", cities['BY']

# print every state abbreviation
print '-' * 10
print 'Print-out of all states and abbreviations'
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s" % (state,abbrev)
	
# print every state abbreviation
print '-' * 10
print 'Print-out of all states and abbreviations'
print '-' * 10
for abbrev, cities in cities.items():
	print "%s state is abbreviated %s" % (state,abbrev)