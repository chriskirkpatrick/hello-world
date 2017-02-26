#!/usr/bin/python

rivers = {
	'nile': 'egypt',
	'rhein': 'germany',
	'danube': 'slovakia'
}

for k, v in rivers.items():
	print("The " + k.title() + " runs through " + v.title())

print("\nRivers:")
for k in rivers.keys():
	print(k.title())

print("\nCountries:")
for v in rivers.values():
	print(v.title())