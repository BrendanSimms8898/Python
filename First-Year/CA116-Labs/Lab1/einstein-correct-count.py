#!/usr/bin/env python

s = raw_input()
count = 0

while s != "end":
    if s[len(s) - 9:] == "incorrect":
        count = count
    elif s[len(s) - 7:] == "correct":
        count = count + 1
    s = raw_input()

print count
