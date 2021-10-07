#!/usr/bin/env python

import func_bsearch

def contains(a, q):
    index = func_bsearch.bsearch(a, q)
    return index <= (len(a) - 1) and q == a[index]
    
if __name__ == '__main__':
    print contains([2,3,6,6,7,8], 1)
    print contains([2,3,6,6,7,8], 2)
    print contains([2,3,6,6,7,8], 6)
    print contains([2,3,6,6,7,8], 8)
    print contains([2,3,6,6,7,8], 9)
    print contains([2,3,6,6,7,8], 4)
