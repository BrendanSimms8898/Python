#!/usr/bin/env python

import func_bsearch

def count(a, q):
    n1 = func_bsearch.bsearch(a, q)
    n2 = func_bsearch.bsearch(a, q + 1)
    count = n2 - n1
    return count

if __name__ == '__main__':
    print count([2, 3, 6, 6, 6, 6, 7, 8], 6)
