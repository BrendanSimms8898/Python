#!/usr/bin/env python

n = raw_input()
a = []

while n != "end":
    a.append(int(n))
    n = raw_input()

p = 0
j = 1    
while j < len(a):
    if a[p] < a[j]:
        p = j
    j = j + 1

print p
