#!/usr/bin/env python

a = []
n = raw_input()
while n != 'end':
   a.append(int(n))
   n = raw_input()

b = []
n = raw_input()
while n != 'end':
   b.append(int(n))
   n = raw_input()


c = a + b

i = 0
while i < len(c):
   p = i
   j = i + 1
   while j < len(c):
      if c[j] < c[p]:
         p = j
      j += 1
   tmp = c[p]
   c[p] = c[i]
   c[i] = tmp
   i += 1
i = 0
while i < len(c):
   print c[i]
   i += 1