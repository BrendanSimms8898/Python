#!/usr/bin/env python

header = raw_input()
s = raw_input()
total = 0

while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i = i + 1
    if s[i + 1:i + 3] == "WI":
        total = total + 1
    s = raw_input()

print total
