#!/usr/bin/env python

i = 0

while i < 10:
    s = raw_input()
    j = 0
    while j < len(s) and (s[j] != "+"):
        j = j + 1

    first = s[:j]
    second = s[j + 1:]
    print int(first) + int(second)
    i = i + 1