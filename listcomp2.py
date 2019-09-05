#!/usr/bin/env python2
#
# Copyright 2019, Michael Pascale
#
# List Comprehensions
# Exercise from ai.berkeley.edu/tutorial.html
#
# Write a list comprehension which, from a list, generates a lowercased version
# of each string that has length greater than five.

continents = ['Antarctica', 'Africa', 'Asia', 'Europe', 'North America', 'South America']

print continents

search_by_length = 5

results = [s.lower() for s in continents if len(s) > search_by_length]

print results
