#!/usr/bin/env python

import sys
words = sys.stdin.read()
words = words.split()

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

i = 0
while i < len(words):
    if words[i] in fruit:
        print words[i]
    i = i + 1
