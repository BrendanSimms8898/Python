#!/usr/bin/env python

n = 8
longest = ""

i = 0
while i <= n - 1:
   line = raw_input()
   if len(longest) < len(line):
      longest = line
   i = i + 1

print longest
