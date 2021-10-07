#!/usr/bin/env python

import sys
nums = sys.stdin.read()
nums = nums.split()

eng = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}

i = 0
while i < len(nums):
    if nums[i] in eng:
        print eng[nums[i]]
    i += 1
