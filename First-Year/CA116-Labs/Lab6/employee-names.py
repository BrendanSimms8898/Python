#!/usr/bin/env python

s = raw_input()
num = []
name = []

while s != "end":
    num.append(s[:8])
    name.append(s[9:])
    s = raw_input()


s = raw_input()
while s != "end":
    i = 0
    while i < len(num):
        if s == num[i]:
            print name[i]
        i = i + 1
    s = raw_input()
