#!/usr/bin/env python

s = raw_input()
a = []
b = []
c = []

while s != "end":
    a.append(int(s))
    s = raw_input()

s = raw_input()

while s != "end":
    b.append(int(s))
    s = raw_input()

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i = i + 1
    else:
        c.append(b[j])
        j = j + 1

if a == []:
    c.append(b)
elif b == []:
    c.append(a)
else:
    print c

i = 0
while i < len(c):
    print c[i]
    i = i + 1
