#!/usr/bin/env python

import sys
words = sys.stdin.read()
words = words.split()

seen = {}
count = 1
i = 0
while i < len(words):
    if words[i] not in seen:
        seen[words[i]] = count
    elif words[i] in seen:
        seen[words[i]] = count + 1
    i += 1

i = 0
while i < len(words):
    if seen[words[i]] == 1:
        print words[i]
    i += 1
