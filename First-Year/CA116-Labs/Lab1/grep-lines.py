#!/usr/bin/env python

import sys
word = sys.argv[1]

line = raw_input()

while line != "end":
    i = 0
    while i < (len(line) - len(word) + 1) and (line[i:i + len(word)] != word):
        i = i + 1
        if i < (len(line) - len(word) + 1):
            print line
        line = raw_input()