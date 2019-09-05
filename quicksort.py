#!/usr/bin/env python2
#
# Copyright 2019, Michael Pascale
#
# Quicksort
# Exercise from ai.berkeley.edu/tutorial.html
#
# Write a quickSort function in Python using list comprehensions.
# Use the first element as the pivot.

from random import shuffle

def quickSort(L):
    if len(L):
        p = L[0]
        l = [i for i in L[1:] if i <= p]
        r = [i for i in L[1:] if i > p]
        quickSort(l)
        quickSort(r)
        while len(L):   # Python uses pass by object reference.
            L.pop()     # Reassigning L would not affect the externally referenced object.
        L.extend(l + [p] + r)

if __name__ == '__main__':
    A = range(10)
    shuffle(A)
    print A

    quickSort(A)
    print A
