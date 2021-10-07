#!/usr/bin/env python

import sys
words = sys.stdin.read()
words = words.split()

seen = {}

i = 0
while i < len(words):
    if words[i] not in seen:
        seen[words[i]] = "one"
        i += 1
    else:
        print "snap: " + words[i]
        i = len(words)
