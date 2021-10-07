#!/usr/bin/env python

s = raw_input()
n = int(s)

i = 0
while i < n and "0" < n[i] or n[i] < "9":

   if n >= 100:
      print n
   else:
      print "none"
   i = i + 1
