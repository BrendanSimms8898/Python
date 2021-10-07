#!/usr/bin/env python

total = 0

while total != 1000:
    s = raw_input()
    j = 0
    while j < len(s) and (s[j] != "+"):
        j = j + 1
    a = s[:j]
    b = s[j + 1:]
    total = int(a) + int(b)
    print total
