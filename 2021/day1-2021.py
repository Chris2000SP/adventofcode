#!/usr/bin/env python3

befor = None
count = 0

for number in [int(line) for line in open('input_Day1_2021')]:
    if befor == None:
        befor = number
        print(str(number) + " N/A")
        continue
    if number < befor:
        print(str(number) + " (decreased)")
    else:
        print(str(number) + " (increased)")
        count += 1
        print("count at " + str(count))
    befor = number

print("\nProgram ended with " + str(count))