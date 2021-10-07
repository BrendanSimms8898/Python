#!/usr/bin/env python

import sys
nums = sys.stdin.read()
nums = nums.split()
a = []
d = {}

with open("translation.txt", "r") as f:
    words = f.read()
    words = words.split()
    i = 0
    while i < len(words):
        eng = words[i]
        ger = words[i + 1]
        k1 = eng
        d[k1] = ger
        i += 2

i = 0
while i < len(nums):
    if nums[i] in d:
        print d[nums[i]]
    i += 1
