#!/usr/bin/python

programming_terms = {
	'variable': 'a placeholder for data',
	'looping': 'iterate through text',
	'dictionary': 'mapping values to keys',
	'list': 'an arbitrary list of values',
	'integer': 'a number that does not have a decimal place',
	}

for key, value in programming_terms.items():
	print(key.title() + "\n\t" + value)