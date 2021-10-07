#!/usr/bin/env python

import sys

enc = {}
n = 13
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLm"

i = 0
while i < len(alpha):
	enc[alpha[i]] = cipher[i]
	i += 1

s = sys.stdin.read()
t = ""
i = 0
while i < len(s):
	if s[i] in enc:
		t = t + enc[s[i]]
	else:
		t = t + s[i]
	i += 1

sys.stdout.write(t)
