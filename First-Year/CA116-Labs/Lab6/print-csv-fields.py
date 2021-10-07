#!/usr/bin/env python

s = raw_input()
a = []

while s != "end":
    a.append(s)
    s = raw_input()

n = input()

j = 0
while j < len(a):
    start = 0
    i = 0
    while i < n:
        while start < len(a[j]) and a[j][start] != ",":
            start = start + 1

        start = start + 1
        i = i + 1

    end = start + 1
    while end < len(a[j]) and a[j][end] != ",":
        end = end + 1

    print a[j][start:end]
    j += 1
