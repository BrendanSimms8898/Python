#!/usr/bin/env python

s = raw_input()
seen = []
words = []

while s != "end":
    words.append(s)
    s = raw_input()

i = 0
while i < len(words):
    j = 0
    while j < len(seen) and seen[j] != words[i]:
        j += 1

    if len(seen) <= j:
        print words[i]
        seen.append(words[i])
    i += 1
