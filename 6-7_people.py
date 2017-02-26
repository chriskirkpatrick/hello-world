#!/usr/bin/python
people = {
	'anais' : {
	  	'first_name': 'x',
  		'last_name': 'x',
  		'age': 'x',
		'city': 'x',
		},
	'chris' : {
		'first_name': 'x',
		'last_name': 'x',
		'age': 'x',
		'city': 'x',
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
