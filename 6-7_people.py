#!/usr/bin/python
people = {
	'anais' : {
	  	'first_name': 'Anais',
  		'last_name': 'van Delft',
  		'age': '35',
		'city': 'Kleve',
		},
	'chris' : {
		'first_name': 'Chris',
		'last_name': 'Kirkpatrick',
		'age': '34',
		'city': 'Kleve',
		},
	'will' : {
		'first_name': 'William',
		'last_name': 'Nylander',
		'age': '20',
		'city': 'Toronto',
		},
	}

for people, info in people.items():
    first_name = info['first_name']
    last_name = info['last_name']
    age = info['age']
    city = info['city']
    print("\nFirst name: " + first_name + "\nLast name: " + last_name + "\nAge: " + age + "\nCity: " + city)