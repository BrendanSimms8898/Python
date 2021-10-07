#!/usr/bin/env python

count = 0
s = raw_input()

i = 0
while i < len(s):
   if (s[i] <= "A" or "Z" <= s[i]):
      count = count + 1
   i = i + 1
print count
