#!/usr/bin/env python

s = raw_input()
name = []
num = []

while s != "end":
	start = 12
	end = start
	while end < len(s) and end != "/":
		end = end + 1
	name.append(s[start:end])
	num.append
	s = raw_input()