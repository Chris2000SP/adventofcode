#!/usr/bin/env python3

befor = None
count = 0

for line in open('input_Day1_2021'):
    if befor == None:
        befor = int(line)
        print(str(line) + " N/A")
        continue
    line = int(line)
    print(type(line))
    if line < befor:
        print(str(line) + " (decreased)")
    else:
        print(str(line) + " (increased)")
        count += 1
        print("count at " + str(count))
    befor = line