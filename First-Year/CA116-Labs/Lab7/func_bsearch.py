#!/usr/bin/env python

def bsearch(a, q):
    low = 0
    high = len(a)
    mid = (high + low) / 2
    while low < high:
        if a[mid] < q:
            low = mid + 1
        else:
            high = mid
        mid = (high + low) / 2

    assert low == 0 or a[low - 1] < q
    assert high == len(a) or q <= a[high]

    return mid

if __name__ == '__main__':
    print bsearch([2, 3, 6, 6, 7, 8], 1)
