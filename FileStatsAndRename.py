'''
    FileStatsAndRename.py

    Prints statistics on a directory of image files named with an index
    number and ASCII value. Optionally rename files so that their numbers
    are ordered.
    
    Copyright 2019, Michael Pascale
'''

import os, math, re

rename = False
path = "/some/path/to/files"
files = os.listdir(path)

symbol = 0
num = 0
bucket = []

def nozero(x):
    return x != 0

for file in files:
    symbol = int(re.search(r'\d+', file).group())
    if symbol > num:
        num = symbol

for i in range(0, num):
    bucket += [0]

print("code\t char\t count")
for file in files:
    symbol = int(re.search(r'\d+', file).group())
    bucket[symbol-1] += 1

i = 0
for item in bucket:
    i += 1
    if item != 0:
        print(i, "\t", chr(i), "\t", item)

print("\nMax:", max(bucket), "Min:", min(filter(nozero, bucket)))
print("\nSum:", sum(bucket))


if rename:
    oldsym = 0
    count = -1
    path2 = "/some/path/to/new/files"
    extension = ".bmp"
    for file in files:
        symbol = int(re.search(r'\d+', file).group())
        if symbol != oldsym:
            count = -1
            oldsym = symbol
        count += 1
        os.rename(path + file, path2 + str(symbol) + "_" + str(count) + extension)
