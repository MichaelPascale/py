'''
    PatchLinesofCode.py
    Counts added lines of code in added in a directory of patch files.
    
    Copyright 2019, Michael Pascale
'''

import os

files = os.listdir()

i = 0

for file in files:
    with open(file) as f:
        for line in f:
            if line[0] is "+":
                if line[1:3] != "++":              
                    i += 1

print(i)
    

